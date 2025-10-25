from flask import Blueprint
auth_bp = Blueprint(
    'auth',                      
    __name__,
    url_prefix='/auth',          
    template_folder='templates', 
    static_folder='static'       
)

# import routes so they register on the blueprint
from . import routes  # noqa: F401
