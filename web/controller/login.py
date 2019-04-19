from managers import app, db
from flask import Blueprint, request, jsonify, redirect
from common.libs.Helper import ops_render
from common.libs.UrlManager import UrlManager
import datetime

route_login = Blueprint('login_page', __name__)


@route_login.route('/', methods=['GET', 'POST'])
def login():
    resp = {'code': 200, 'msg': '登录成功'}
    if request.method == 'GET':
        return ops_render('admin/login.html')

    return jsonify(resp)

@route_login.route('/vaild', methods=['POST'])
def login_valid():
    resp = {'code': 200, 'msg': '登录成功'}
    return jsonify(resp)
