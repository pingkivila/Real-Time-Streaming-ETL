#import pyspark
#from pyspark.sql import SparkSession
#from pyspark.sql.functions import explode
#from pyspark.sql.functions import split
#from pyspark.sql.types import StructType,StructField, StringType, IntegerType, TimestampType

import time
import json
import pandas as pd
from kafka import KafkaConsumer
from pandas import DataFrame
from datetime import datetime
from jsonpath_ng import jsonpath, parse
from datetime import datetime

brokers='localhost:9092'
topic='weathermap_topic'
sleep_time=5
offset='latest'

consumer = KafkaConsumer(bootstrap_servers=brokers, auto_offset_reset=offset,consumer_timeout_ms=1000)
consumer.subscribe([topic])

list_header = ['temp','weather','datetime','city']
newdf33 = pd.DataFrame(data = [], columns=[list_header])
newdf33.to_csv('csv_data.csv', mode='a', header=True)

def GetListOfSubstrings(stringSubject,string1,string2):
    MyList = []
    intstart=0
    strlength=len(stringSubject)
    continueloop = 1

    while(intstart < strlength and continueloop == 1):
        intindex1=stringSubject.find(string1,intstart)
        if(intindex1 != -1): #The substring was found, lets proceed
            intindex1 = intindex1+len(string1)
            intindex2 = stringSubject.find(string2,intindex1)
            if(intindex2 != -1):
                subsequence=stringSubject[intindex1:intindex2]
                MyList.append(subsequence)
                intstart=intindex2+len(string2)
            else:
                continueloop=0
        else:
            continueloop=0
    return MyList
        
jsonpath_expression1 = parse('$.main.temp')
jsonpath_expression2 = parse('$.weather.[0].main')
jsonpath_expression3 = parse('$.dt')
jsonpath_expression4 = parse('$.name')

        
#message.headers['content-type']
#message.encoding
#message.text

master = ''
while(True):
    for message in consumer:
        master = str(message.value)
        List = GetListOfSubstrings(master,"""b'""", """'""")
        for x in range(0, len(List)):
            master2=(List[x])
        json_data = json.loads(master2)

        for match in jsonpath_expression1.find(json_data): 
            temp = match.value
            df = pd.DataFrame(data=[{temp}],columns=['temp'])

        for match2 in jsonpath_expression2.find(json_data):
            weather = match2.value
            df2 = pd.DataFrame(data=[{weather}],columns=['weather'])

        for match3 in jsonpath_expression3.find(json_data):
            ts=int(f'{match3.value}')
            tanggal = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            df3 = pd.DataFrame(data=[{tanggal}],columns=['tanggal'])

        for match4 in jsonpath_expression4.find(json_data):
            city = match4.value
            df4 = pd.DataFrame(data=[{city}],columns=['city'])

        dfbaru = df.join(df3)
        dfbaru2 = df2.join(df4)
        newdfff = dfbaru.join(dfbaru2)
        print(newdfff)
        
        newdfff.to_csv('csv_data.csv', mode='a', header=False)

