from flask_restplus import fields

from app.api.v1 import namespace

login_schema = namespace.model(
    "Login",
    {
        "access_token": fields.String(),
        "refresh_token": fields.String(),
    },
)

signup_schema = namespace.model(
    "SignUp",
    {
        "id": fields.String(),
        "login": fields.String(),
        "email": fields.String(),
        "is_active": fields.Boolean(),
    },
)

user_history_schema = namespace.model(
    "UserHistory",
    {
        "id": fields.String(),
        "timestamp": fields.DateTime(),
        "user_agent": fields.String(),
        "ip_addr": fields.String(),
        "device": fields.String(),
    },
)
