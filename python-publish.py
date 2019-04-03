import time
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

publish_key = 'pub-c-e07b6085-b36b-4caa-9e32-abda06f7f47c'

subscribe_key = 'sub-c-ad06a870-54f8-11e9-93f3-8ed1bbcba485'

secret_key = 'sec-c-MjJmZmJmZmQtZDZiNS00NTVkLWIyYmQtMjg0NzczZjE5M2U0'

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
