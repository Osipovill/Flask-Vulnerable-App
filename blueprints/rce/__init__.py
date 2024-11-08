from flask import Blueprint

rce_bp = Blueprint('rce', __name__, template_folder='src', url_prefix='/rce')

from . import routes
