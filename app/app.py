from flask import Flask
from datetime import timedelta
from app.pubnubclient import pubnub_client

subscribe_key = "sub-c-cd0b6288-cdf5-11e5-bcee-0619f8945a4f"
publish_key = "pub-c-37d3c709-c35e-487a-8b33-2314d9b62b28"
secret_key = None


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    pubnub_client.init_client(subscribe_key, publish_key, secret_key)

    if secret_key:
        pubnub_client.establish_grants(
            user='user-id-123890',
            channels=['test-channel'],
            ttl=timedelta(days=3)
        )

    @app.route("/send")
    def send():
        pubnub_client.send_message("test-channel", "hey")
        return "OK", 200

    return app
