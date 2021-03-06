APP = {
    'domain': 'http://127.0.0.1:5000'
}

UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'],
    'prefix_path': '/web/static/upload/',
    'prefix_url': '/static/upload/'
}

IGNORE_URLS = [
    "^/admin/login",
    "^/admin/store/get",
    "^/"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]

AUTH_COOKIE_NAME = 'UserCookie'
SERVER_PORT = '5000'
SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bryant:leekobe24@cd-cdb-gf49lo9s.sql.tencentcdb.com:63247/petsanima'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_ENCODING = "utf8mb4"
SQLALCHEMY_BINDS = {
    'wechat': "mysql+pymysql://bryant:leekobe24@cd-cdb-gf49lo9s.sql.tencentcdb.com:63247/petsanima"
}