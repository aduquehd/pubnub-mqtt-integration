import time
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

from pubnub_data import publish_key, subscribe_key, channel_name

pnconfig = PNConfiguration()
pnconfig.publish_key = publish_key
pnconfig.subscribe_key = subscribe_key
pubnub = PubNub(pnconfig)

javascript_timetoken = int(time.time() * 1000)

names = ['andres', 'nelson', 'ana', 'didier', 'rodrigo']
# names = ['andres']
for name in names:
    pubnub.publish().channel("Channel-mpov50b6x").message({
        'tt': javascript_timetoken,
        'foo': 'bar',
        'name': name
    }).sync()
