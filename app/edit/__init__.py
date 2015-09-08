from flask import Blueprint

editor = Blueprint('edit', __name__)

from . import views
