import requests
import time
import json 
from confluent_kafka import Producer
import socket
import os

conf = {'bootstrap.servers': f"{os.environ.get(kafka_bootstrap_server)}",
        'security.protocol': 'SASL_SSL',
        'sasl.mechanism': 'PLAIN',
        'sasl.username': f"{os.environ.get(sasl_username)}",
        'sasl.password': f"{os.environ.get(sasl_password)}",
        'client.id': socket.gethostname()}

producer = Producer(conf)


API_KEY=f"{os.environ.get(f_hub_api)}"

BASE_URL="https://finnhub.io/api/v1"


EXCHANGE="US"
MIC="XNYS"

SYMBOLS=['JPM','BAC','GS','WFC']

# producer= KafkaProducer(bootstrap_servers='localhost:9092',api_version=(2,3,0),  value_serializer=lambda v: json.dumps(v).encode("utf-8"))

# def testkafkaconnection():
#     try:
#         admin = KafkaAdminClient(
#             bootstrap_servers="localhost:9092",
#             api_version=(2,3,0)
#         )
#         print("Connected! Brokers:", admin.list_topics())
#     except Exception as e:
#         print("Failed:", e)


# # testkafkaconnection()



def fetch(symbol):
    url=f"{BASE_URL}/quote?symbol={symbol}&token={API_KEY}"
    try:
        print(url)
        data=requests.get(url)
        response=data.json()
        response['symbol']=symbol
        response['fetched_at']=int(time.time())
        return response
    except Exception as e:
        print(f"Error fetching: {e}")
        return None
    

for i in range(1,5):
    for symbol in SYMBOLS:
        quote=fetch(symbol)
        if quote:
            print(f"producing: {quote}")
            producer.produce("my-stock-data",json.dumps(quote).encode("utf-8"))
    time.sleep(5)
    

    





