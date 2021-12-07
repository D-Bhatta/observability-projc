**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

DONE.

## Setup the Jaeger and Prometheus source
DONE

## Create a Basic Dashboard
DONE

## Describe SLO/SLI

### SLO example:

- Our APIs should not take more than 10 seconds to return data more than 24 times a month.

### SLI example:

- Our APIs took a total of 320 extra seconds to return data, exceeding our latency budget by 80 seconds. We net a 98% uptime.

Here, the SLO is not exceeding latency of 10 seconds more than 24 times in a given month. This aims to ensure service satisfcation among customers, who are then assured a monthly uptime of 99.9%, and will get a response from our APIs within 10 seconds.

The actual SLI is a latency budget of 240 seconds a month, which translates to 99.9% uptime. Our actual measure was keeping track of how long it took to return a request, find the times we exceeded 10s, and adding it up till the end of the month. The SLI is something we actually measured, while the SLO was a goal here we had to meet, and by this example, failed to meet by 80 seconds this month across our customer base. Therefore, we can say that the indicator was how lond it took to serve a request, and the objective was to have high monthly uptime and low latency for our APIS.

## Creating SLI metrics.

- Latency of API response: How long it takes to get a response, which affects the operation of dependants on the API. If the latency is too high, dependants will abandon the API for something with lower latency.
- Success rates: Success rates measured by the 20X or 30X response code.
- Page load time: a customer shoudl only spend a few seconds for a webpage to load, otherwise it will cause disatisfaction.
- Error rates: We should measure our 40X and 50X error rates and ensure that the error is below a threshold level.
- Saturation: Saturation can mean that load is not being evenly distributed or resources might need scaling.

## Create a Dashboard to measure our SLIs
DONE.

## Tracing our Flask App
DONE.

## Jaeger in Dashboards
DONE.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue also include a screenshot of the tracer span to demonstrate how we can user a tracer to locate errors easily.

TROUBLE TICKET

Name: Debabrata Bhattacharya

Date: 6th December

Subject: High 404 

Affected Area: Backend API

Severity: High

Description:
The Backend API is geeting a lot of 404 errors due to user error. The file corresponding to that section is `backend\app.py`. Screenshot in answer-img under `span-trace-errors.png`.


## Creating SLIs and SLOs

1. Latency: Latency is often the indication of an inefficient system. Decreasing latency will incrementally improve the code base and improve the reliability of the system.
2. Saturation: Constant saturation denotes resource scarcity, which can cause downtime due to not enough resources for the applications to run.
3. The amount of traffic throughput  is a good indicator to measure. Increasing availability will prevent peak traffoc to cause downtime.
4. Error rate. Having a high error rate directly corresponds to increased downtime.

## Building KPIs for our plan


- Node resource utilization: IO, Memory, and CPU usage across each node.
- Latency: Latency of the response across services.
- Error rate: Error rate across the clusters.
- Saturation: Saturation of resources across the network in terms of number of pods.



## Final Dashboard
DONE.