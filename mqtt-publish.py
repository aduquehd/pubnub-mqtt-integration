import paho.mqtt.client as mqtt
import json

publish_key = 'pub-c-ce2f1ab4-1cf1-45ba-9042-47fe5181375b'

subscribe_key = 'sub-c-6a92f46c-54da-11e9-bacd-ba825bfe5cc2'

secret_key = 'sec-c-MjJmZmJmZmQtZDZiNS00NTVkLWIyYmQtMjg0NzczZjE5M2U0'

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
