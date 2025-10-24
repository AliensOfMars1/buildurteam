from flask import Blueprint

messages_bp = Blueprint(
    'messages_bp',
    __name__,
    url_prefix='/messages',
    template_folder='templates',
    static_folder='static'
)

from . import routes # noqa: F401