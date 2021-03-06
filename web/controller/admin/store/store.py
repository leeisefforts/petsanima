from web.controller.admin import route_admin
from managers import app, db
from common.libs.Helper import ops_render, getCurrentDate
from common.libs.UrlManager import UrlManager
from common.models.store.Store_Member import Store_Member
from flask import jsonify, request, redirect


@route_admin.route('/store', methods=['GET', 'POST'])
def store_index():
    if request.method == 'GET':
        return ops_render('admin/store/store.html')


@route_admin.route('/store/set', methods=['GET', 'POST'])
def store_set():
    if request.method == 'GET':
        return ops_render('admin/store/store_set.html')


@route_admin.route('/store/get', methods=['GET', 'POST'])
def store_get():
    resp = {'code': 200, 'msg': 'success'}
    req = request.values
    if request.method == 'GET':
        sid = req['sid'] if 'sid' in req else 0
        resp['store_id'] = sid
        return ops_render('admin/store/store_get.html', resp)

    pet_name = req['pet_name'] if 'pet_name' in req else ''
    pet_age = req['pet_age'] if 'pet_age' in req else 0
    pet_sex = req['pet_sex'] if 'pet_sex' in req else 0
    host_phone = req['host_phone'] if 'host_phone' in req else ''
    host_name = req['host_name'] if 'host_name' in req else ''
    store_id = req['id'] if 'id' in req else 0

    sm = Store_Member()
    sm.status = 1
    sm.store_id = store_id
    sm.petname = pet_name
    sm.petage = pet_age
    sm.petsex = pet_sex
    sm.hostname = host_name
    sm.hostphone = host_phone
    sm.created_time = getCurrentDate()
    sm.updated_time = getCurrentDate()
    db.session.add(sm)
    db.session.commit()

    return ops_render('admin/store/store_success.html')
