import paho.mqtt.client as mqtt
import json

from .pubnub_data import publish_key, subscribe_key, channel_name

client_uuid = "6e19d4d9-1037-435e-814f-ea242bf07a35"

publish_key = publish_key
subscribe_key = subscribe_key
client_id = client_uuid
print("Starting")


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


client = mqtt.Client(client_id=publish_key + "/" + subscribe_key + "/" + client_id)
client.publish("Channel-ish3r1xed", json.dumps({"asdgas": 1235125}))
