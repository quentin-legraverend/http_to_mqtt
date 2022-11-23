# http_to_mqtt

Simple API for HTTP to MQTT. Based on [jpowcode article and code](http://jpowcode.com/http_to_mqtt.html)(link seems down now).

To send message `d` in topic `office/blinds`:
```
http://127.0.0.1:5000/mqtt?topic=office/blinds&message=d&token=changeme
```

1. Run server locally:
```
git clone
pip install -r requirements.txt
python app.py
```
for a more "cleaner" way you would use virtualenv for Python.

2. Run server on docker:
```
docker run -e MQTT_HOST=127.0.0.1 -e BIND_HOST=0.0.0.0 -e API_TOKEN=changeme -p 5000:5000 kuaaaly/http-to-mqtt:latest
```
API_TOKEN stands here to "secure" the connection.
It is a very basic mechanism which is vulnerable to MitM attack.
You can use the following environment variables (those are defaults):
```
MQTT_HOST = 127.0.0.1
MQTT_PORT = 1883
BIND_HOST = 127.0.0.1
BIND_PORT = 5000
API_TOKEN = MY_TOKEN
```
