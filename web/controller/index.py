from managers import app, db
from flask import Blueprint
from common.libs.Helper import ops_render
import datetime

route_index = Blueprint('index_page', __name__)


@route_index.route('/')
def index():
    return ops_render('index.html')
