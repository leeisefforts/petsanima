from flask import Blueprint

route_admin = Blueprint('admin_page', __name__)

from web.controller.admin.index import *
from web.controller.admin.store.store import *
from web.controller.admin.account.account import *