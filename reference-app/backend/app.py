from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import logging

# Replace mongodb with an in memory dict

stars = {}

from prometheus_flask_exporter.multiprocess import GunicornInternalPrometheusMetrics
from flask_opentracing import FlaskTracing
from jaeger_client import Config
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from prometheus_flask_exporter import PrometheusMetrics

from os import getenv

JAEGER_HOST = getenv('JAEGER_HOST', 'localhost')

FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()
metrics = PrometheusMetrics(app)
# static information as metric
metrics.info("app_info", "Application info", version="1.0.3")
common_counter = metrics.counter(
    'by_endpoint_counter', 'Request count by endpoints',
    labels={'endpoint': lambda: request.endpoint}
)

logging.getLogger("").handlers = []
logging.basicConfig(format="%(message)s-%(asctime)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)

def init_tracer(service):

    config = Config(
        config={
            "sampler": {"type": "const", "param": 1},
            "logging": True,
            "reporter_batch_size": 1,
            'local_agent':
            # Also, provide a hostname of Jaeger instance to send traces to.
            {'reporting_host': JAEGER_HOST}},
        service_name=service,
        validate=True,
        metrics_factory=PrometheusMetricsFactory(service_name_label=service),
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()


tracer = init_tracer("backend")
flask_tracer = FlaskTracing(tracer, True, app)


@app.route("/")
@common_counter
def homepage():
    with tracer.start_span("req-home") as homepage_span:
        logger.info("Display welcome page")
        homepage_span.set_tag("http.status_code", 200)
    return "Hello World"


@app.route("/api")
@common_counter
def my_api():
    with tracer.start_span("req-api") as api_span:
        answer = "something"
        api_span.set_tag("http.status_code", 200)
        api_span.set_tag("api.result", answer)
        logger.info(f"PIR result returned 200 with payload {answer}")
    return jsonify(repsonse=answer)


@app.route("/star", methods=["POST"])
@common_counter
def add_star():
    with tracer.start_span("req-api-post") as api_post_span:
        name = request.json["name"]
        distance = request.json["distance"]
        star_id = len(stars) + 1

        new_star = {
            "_star_id": star_id,
            "name": name,
            "distance": distance
        }
        stars[star_id] = new_star
        output = {"name": new_star["name"], "distance": new_star["distance"]}
        logger.info(f"Saved in memory: {output}")
        api_post_span.set_tag("http.status_codes", 200)
        api_post_span.set_tag("api_post_span.output", 200)
    return jsonify({"result": output})

    # register additional default metrics
metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)


if __name__ == "__main__":
    app.run()
