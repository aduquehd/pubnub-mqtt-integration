import paho.mqtt.client as mqtt

from .pubnub_data import publish_key, subscribe_key, channel_name

client_uuid = 'MacDevice2'

topic = publish_key + "/" + subscribe_key + "/" + channel_name
mqtt_connect = publish_key + "/" + subscribe_key + "/" + client_uuid


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))
    client.subscribe(topic, 0)


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


client = mqtt.Client(client_id=mqtt_connect)

client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe

client.connect("mqtt.pndsn.com", 1883, 60)

client.loop_forever()
