**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation
![Pods and Services](./answer-img/01_PodSvc.png)

## Setup the Jaeger and Prometheus source
![Grafana Home](./answer-img/02_Grafana-Home.png)

## Create a Basic Dashboard
![Grafana Prometheus](./answer-img/03_Grafana-Prometheus.png)

## Describe SLO/SLI
SLO: *monthly uptime* - SLI: 99.5% of all requests in one month are answered successfully

SLO: *request response time* - SLI: 99% of requests have a latency of less than 100ms

## Creating SLI metrics.
1. Availability
    - Percentage of successfully answered requests in a day
2. Errors
    - Number of HTTP 5xx responses per week
3. Average Latency
    - Average response times for requests by the customer in a day
4. Percentage of Slow Responses
    - Percentage of response times slower than a threshold in a day
5. Hardware Limitations
    - Maximum CPU usage in one hour. 

## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here. Also provide a (screenshot) sample Python file containing a trace and span code used to perform Jaeger traces on the backend service.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name four SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create a list of 2-3 KPIs to accurately measure these metrics as well as a description of why those KPIs were chosen. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
