from flask import Blueprint

projects_bp = Blueprint(
    'projects_bp',
    __name__,
    url_prefix='/projects',
    template_folder='templates',
    static_folder='static' 
)
 
from . import routes # noqa: F401