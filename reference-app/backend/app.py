import random
import time
from flask import Flask, render_template, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from jaeger_client import Config
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory

import logging
import pymongo
from flask_pymongo import PyMongo

app = Flask(__name__)
PrometheusMetrics(app)

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

mongo = PyMongo(app)

#################
# jaeger config #
#################


def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    config = Config(
        config={
            "sampler": {"type": "const", "param": 1},
            "logging": True,
            "reporter_batch_size": 1,
        },
        service_name=service,
        validate=True,
        metrics_factory=PrometheusMetricsFactory(service_name_label=service),
    )
    return config.initialize_tracer()


tracer = init_tracer('backend-tracer')


@app.route("/")
def homepage():
    s = 'HelloWorld'
    with tracer.start_span('hello-world') as span:
        span.log_kv({'event': 'say hello', 'value': s})
        return s


@app.route("/api")
def my_api():
    answer = "something"
    with tracer.start_span('api') as span:
        # wait a random timespan to simulate some work
        wait_time = random.uniform(0, 3)
        span.log_kv({'event': 'start working', 'answer': answer})
        time.sleep(wait_time)
        # raise an error for testing puroses in a small number of cases:
        if random.random() < 0.05:
            raise IndexError('some index is out of bounds!') # I'll use this for the sample ticket Todo
        span.log_kv({'event': 'done some work', 'time': wait_time})
        return jsonify(repsonse=answer)


@app.route("/star", methods=["POST"])
def add_star():
    with tracer.start_span('api') as span:
        star = mongo.db.stars
        name = request.json["name"]
        distance = request.json["distance"]
        try:
            star_id = star.insert({"name": name, "distance": distance})
            new_star = star.find_one({"_id": star_id})
            output = {"name": new_star["name"],
                      "distance": new_star["distance"]}
            span.log_kv({'event': 'New Star', 'result': output})
            return jsonify({"result": output})
        except TypeError:
            span.log_kv({'event': 'Error creating new star', 'answer': 'TypeError'})
            return jsonify({"result": "Error", "message": "TypeError occured"})

# error route to fill the dashboard


@app.route("/500")
def error500():
    return 'server error for testing', 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
