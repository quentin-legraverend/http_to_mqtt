# http_to_mqtt

Simple HTTP "API" to MQTT server. Based on [jpowcode article and code](http://jpowcode.com/http_to_mqtt.html).

Usage example:
- You want to send message: `d` in topic: `office/blinds`. Just do `http://127.0.0.1:5000/mqtt?topic=office/blinds&message=d` in your favorite web browser and you are done.

1. Run server locally:
```
1. git clone
2. pip install -r requirements.txt
3. python app.py
```
for a more "cleaner" way you would use virtualenv for Python.

2. Run server on docker:
```
docker run -e MQTT_HOST=127.0.0.1 -e BIND_HOST=0.0.0.0 -p 5000:5000 kuaaaly/http-to-mqtt:latest
```

You can use the following environement variables (those are defaults):
```
MQTT_HOST = 127.0.0.1
MQTT_PORT = 1883
BIND_HOST = 127.0.0.1
BIND_PORT = 5000
```
