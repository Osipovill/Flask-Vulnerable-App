from flask import Blueprint

xss_bp = Blueprint('xss', __name__, template_folder='src', url_prefix='/xss')

from . import routes
