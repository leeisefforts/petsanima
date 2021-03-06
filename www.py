from managers import app

'''
统一拦截处理和统一错误处理
'''
from web.interceptors.AuthInterceptor import *
from web.interceptors.ApiAuthInterceptor import *
from web.interceptors.ErrortInterceptor import *

from web.controller.index import route_index
from web.controller.login import route_login
from web.controller.static import route_static
from web.controller.admin import route_admin

app.register_blueprint(route_index, url_prefix="/")
app.register_blueprint(route_login, url_prefix="/login")
app.register_blueprint(route_static, url_prefix="/static")
app.register_blueprint(route_admin, url_prefix="/admin")
