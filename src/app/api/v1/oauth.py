from datetime import datetime
from uuid import uuid4

from app.datastore import user_datastore
from flask import url_for, request, jsonify
from flask_restplus import Resource
from werkzeug import exceptions

from app.api.v1 import namespace
from app.database import session_scope
from app.models import SocialAccount
from app.oauth import oauth
from app.services.accounts import AccountsService
from app.services.storages import TokenStorageError
from app.services.oauth_service import oauthorization


@namespace.route("/login/<string:name>")
class OauthLoginView(Resource):
    @namespace.doc("oauth login")
    def get(self, name: str):
        client = oauth.create_client(name)

        if not client:
            raise exceptions.NotFound()

        redirect_url = url_for("Api v1_oauth_authorization_view", name=name, _external=True)

        return client.authorize_redirect(redirect_url)


@namespace.route("/auth/<string:name>")
class OauthAuthorizationView(Resource):
    @namespace.doc("oauth authorization")
    def get(self, name: str):
        client = oauth.create_client(name)

        if not client:
            raise exceptions.NotFound()

        token = oauthorization(client, name)

        return token
