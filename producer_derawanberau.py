import sys
#!{sys.executable} -m pip install kafka-python
import time
import json
from json import dumps
from kafka import KafkaProducer
from time import sleep
import requests as req

derawan_berau="http://api.openweathermap.org/data/2.5/weather?id=1623024&appid=6afa72ee728492b6960489dfba7a472a&units=metric"
brokers='localhost:9092'
topic='weather_topic'
sleep_time=0

producer = KafkaProducer(bootstrap_servers=[brokers],value_serializer=lambda x: dumps(x).encode('utf-8'))

while(True):
    print("Getting new data...")
    resp = req.get(derawan_berau)
    json_data = json.loads(resp.text)
    producer.send(topic, json_data)
    time.sleep(sleep_time)

