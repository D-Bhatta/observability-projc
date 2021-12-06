**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for all components. Take a screenshot of the output and include it here to verify the installation

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheus as a data source. Provide a screenshot of the home page after logging into Grafana.

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

### SLO example:

- Our APIs should not take more than 10 seconds to return data more than 24 times a month.

### SLI example:

- Our APIs took a total of 320 extra seconds to return data, exceeding our latency budget by 80 seconds. We net a 98% uptime.

Here, the SLO is not exceeding latency of 10 seconds more than 24 times in a given month. This aims to ensure service satisfcation among customers, who are then assured a monthly uptime of 99.9%, and will get a response from our APIs within 10 seconds.

The actual SLI is a latency budget of 240 seconds a month, which translates to 99.9% uptime. Our actual measure was keeping track of how long it took to return a request, find the times we exceeded 10s, and adding it up till the end of the month. The SLI is something we actually measured, while the SLO was a goal here we had to meet, and by this example, failed to meet by 80 seconds this month across our customer base. Therefore, we can say that the indicator was how lond it took to serve a request, and the objective was to have high monthly uptime and low latency for our APIS.

## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs.

- Latency of API response: How long it takes to get a response, which affects the operation of dependants on the API. If the latency is too high, dependants will abandon the API for something with lower latency.
- Success rates: Success rates measured by the 20X or 30X response code.
- Page load time: a customer shoudl only spend a few seconds for a webpage to load, otherwise it will cause disatisfaction.
- Error rates: We should measure our 40X and 50X error rates and ensure that the error is below a threshold level.
- Saturation: Saturation can mean that load is not being evenly distributed or resources might need scaling.

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
