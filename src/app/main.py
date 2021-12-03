from flask import Flask
from flask_opentracing import FlaskTracer

from app.api import init_api
from app.cache import init_cache
from app.database import init_db
from app.datastore import init_datastore
from app.jwt import init_jwt
from app.oauth import init_oauth
from app.settings import settings
from app.middlewares import init_rate_limit, init_trace

app = Flask(settings.FLASK_APP)
app.config["DEBUG"] = settings.DEBUG
app.config["SECRET_KEY"] = settings.SECRET_KEY


init_trace(app)
init_rate_limit(app)
init_db(app)
init_datastore(app)
init_oauth(app)
init_api(app)
init_jwt(app)
init_cache(app)

app.app_context().push()
