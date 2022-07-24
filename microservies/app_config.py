# Application params
APP_NODE = "app.main:app"
APP_PORT = 7125
APP_HOST = "127.0.0.1"

# database params
MONGO_USER = "amitstartupuser"
MONGO_SERVER = "amitstartup.hopto.org"
MONGO_PORT = 27277
MONGO_PASSWORD = "amit1startup2user"
MONGO_DB = "test"
MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_SERVER}:{MONGO_PORT}/{MONGO_DB}"
