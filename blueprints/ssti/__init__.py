from flask import Blueprint

ssti_bp = Blueprint('ssti', __name__,  template_folder='src', url_prefix='/ssti')

from . import routes
