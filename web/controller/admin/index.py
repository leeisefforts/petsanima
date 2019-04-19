from web.controller.admin import route_admin
from common.libs.Helper import ops_render

from flask import jsonify, render_template


@route_admin.route('/')
@route_admin.route('/index')
def admin_index():
    resp = {'code': 200, 'msg': '登录成功'}
    return ops_render('admin/index.html', resp)
