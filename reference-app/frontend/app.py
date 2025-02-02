from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
PrometheusMetrics(app)


@app.route("/")
def homepage():
    return render_template("main.html")

# error route to fill the dashboard
@app.route("/500")
def error500():
    return 'server error for testing', 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
