from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration


def publish_callback(envelope, status):
    if not status.is_error():
        print(str(envelope) + '\n')
        print("STATUS:" + str(status.status_code) + '\n\n')
    else:
        print("ERROR: ")
        print(str(status.error_data.information) + '\n\n')


PUBNUB_PRESENCE_CHANNEL_SUFFIX = 'pnpres'


class PubNubClient(object):

    def init_client(self, subscribe_key, publish_key, secret_key=None):

        self.pnconfig = PNConfiguration()
        self.pnconfig.subscribe_key = subscribe_key
        self.pnconfig.publish_key = publish_key
        self.pnconfig.secret_key = secret_key
        self.pnconfig.ssl = True
        self.client = PubNub(self.pnconfig)

    def send_message(self,
                     pubnub_channel,
                     payload):
        """Send a message to users subscribed to any of the channels."""
        self.client \
            .publish() \
            .channel(pubnub_channel) \
            .message(payload) \
            .async(publish_callback)

    def establish_grants(self, user, channels, ttl):

        self.client.grant(). \
            read(True). \
            write(False). \
            manage(False). \
            channels(channels). \
            auth_keys(user). \
            ttl(int(ttl.total_seconds() / 60)). \
            sync()
        return {"subscribe_key": self.pnconfig.subscribe_key,
                "publish_key": self.pnconfig.publish_key,
                "pam_key": user}


pubnub_client = PubNubClient()
