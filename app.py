import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration

pnconfig = PNConfiguration()

pnconfig.subscribe_key = "sub-c-cd0b6288-cdf5-11e5-bcee-0619f8945a4f"
pnconfig.publish_key = "pub-c-37d3c709-c35e-487a-8b33-2314d9b62b28"

pubnub = PubNub(pnconfig)

logs = open('logs.txt', 'w')

def publish_callback(envelope, status):
    if not status.is_error():
        logs.write(str(envelope) + '\n')
        logs.write("STATUS:" + str(status.status_code) + '\n\n')
    else:
        logs.write("ERROR: ")
        logs.write(str(status.error_data.information) + '\n\n')

while(True):
    time.sleep(1)
    pubnub.publish().channel("test-channel").message("hey").async(publish_callback)

