from web.controller.admin import route_admin
from common.libs.Helper import ops_render

from flask import jsonify, render_template


@route_admin.route('/account', methods=['GET', 'POST'])
def account_index():
    return ops_render('admin/account.html')


