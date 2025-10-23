
from flask import Blueprint

# blueprint name is "auth" (this determines url_for endpoint prefix)
auth_bp = Blueprint(
    'auth',                      
    __name__,
    url_prefix='/auth',          # all routes will live under /auth/...
    template_folder='templates', 
    static_folder='static'       
)

# import routes so they register on the blueprint
from . import routes  # noqa: F401
