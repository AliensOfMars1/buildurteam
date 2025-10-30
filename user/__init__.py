

from flask import Blueprint

user_bp = Blueprint(
    'user',
    __name__,
    url_prefix='/user',
    template_folder='templates',
    static_folder='static'
)

from . import routes