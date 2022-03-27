import sys
#!{sys.executable} -m pip install kafka-python
import time
import json
from json import dumps
from kafka import KafkaProducer
from time import sleep
import requests as req

ntb="http://api.openweathermap.org/data/2.5/weather?id=1633792&appid=6afa72ee728492b6960489dfba7a472a&units=metric"
brokers='localhost:9092'
topic='weathermap_topic'
sleep_time=5

producer = KafkaProducer(bootstrap_servers=[brokers],value_serializer=lambda x: dumps(x).encode('utf-8'))

while(True):
    print("Getting new data...")
    resp = req.get(ntb)
    json_data = json.loads(resp.text)
    producer.send(topic, json_data)
    time.sleep(sleep_time)
