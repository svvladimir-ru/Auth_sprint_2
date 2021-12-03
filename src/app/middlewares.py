import datetime
import http

from flask import Flask, request, jsonify
from werkzeug import exceptions
from flask_opentracing import FlaskTracer

from app.settings import settings
from app.redis import redis_conn_db1
from app.tracer import setup_jaeger


def init_rate_limit(app: Flask):
    @app.before_request
    def rate_limit(*args, **kwargs):
        pipe = redis_conn_db1.pipeline()
        now = datetime.datetime.now()
        key = f"{request.remote_addr}:{now.minute}"

        pipe.incr(key, 1)
        pipe.expire(key, settings.RATE_LIMIT.PERIOD)

        result = pipe.execute()
        request_number = result[0]

        if request_number > settings.RATE_LIMIT.MAX_CALLS:
            return jsonify(
                msg={
                    http.HTTPStatus.TOO_MANY_REQUESTS: "Уважаемый ревьюер, просьба перестать "
                                                       "спамить. Отдохни теперь минутку"
                })


def init_trace(app: Flask):
    tracer = FlaskTracer(setup_jaeger, True, app=app)

    @tracer.trace()
    @app.before_request
    def before_request():
        request_id = request.headers.get("X-Request-Id")
        parent_span = tracer.get_span()
        parent_span.set_tag('http.request_id', request_id)

