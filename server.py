import os
import sentry_sdk
from bottle import Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://a0c126928aad4edcb31e0396efefe359@sentry.io/4280183",
    integrations=[BottleIntegration()]
)

server = Bottle()

@server.route("/")
def index():    
    return "индекс"

@server.route("/success")
def success():    
    return "Сакцес"

@server.route("/fail")
def fail():
    raise RuntimeError("Ошибка")  
    return

if os.environ.get("APP_LOCATION") == "heroku":
    server.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    server.run(host='localhost', port=8080, debug=True)