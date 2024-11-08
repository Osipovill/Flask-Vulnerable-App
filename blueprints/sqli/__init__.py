from flask import Blueprint

sqli_bp = Blueprint('sqli', __name__, template_folder='src', url_prefix='/sqli')

from . import routes
