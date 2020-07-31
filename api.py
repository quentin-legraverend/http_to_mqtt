import os
import paho.mqtt.client as mq

from flask import Flask, request

MQTT_HOST = os.getenv('MQTT_HOST', '127.0.0.1')
MQTT_PORT = os.getenv('MQTT_PORT', 1883)
BIND_HOST= os.getenv('BIND_HOST', '127.0.0.1')
BIND_PORT = os.getenv('BIND_PORT', 5000)
API_TOKEN = os.getenv('API_TOKEN', 'MY_TOKEN')

app = Flask(__name__)

@app.route('/mqtt', methods=['GET'])

def get_id():

    topic = request.args.get('topic')
    message = request.args.get('message')
    token = request.args.get('token')
    if token == API_TOKEN:
        mqtt = mq.Client("http-to-mqtt")
        mqtt.connect(MQTT_HOST, MQTT_PORT, 15)
        mqtt.publish(topic, message)
        return 'MQTT command published'
    else:
        return 'Wrong API_TOKEN specified'

if __name__ == '__main__':
    print("Starting HTTP-to-MQTT server. MQTT_HOST is: {}:{}".format(MQTT_HOST, MQTT_PORT))
    app.run(host= BIND_HOST, port= BIND_PORT)
