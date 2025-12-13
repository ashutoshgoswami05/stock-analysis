import requests
import time
import json 
import boto3
import os
from confluent_kafka import Consumer
import sys

conf = {'bootstrap.servers': os.environ.get("kafka_bootstrap_server"),
        'security.protocol': 'SASL_SSL',
        'sasl.mechanism': 'PLAIN',
        'sasl.username': os.environ.get("sasl_username"),
        'sasl.password': os.environ.get("sasl_password"),
        'group.id': 'consumer',
        'enable.auto.commit': 'false',
        'auto.offset.reset': 'earliest'}

consumer = Consumer(conf)

# consumer= KafkaConsumer('my-stock-data',group_id="my-stock-group-1",bootstrap_servers='localhost:9092',api_version=(2,3,0),auto_offset_reset="earliest",
#    enable_auto_commit=True, value_deserializer=lambda v: json.loads(v.decode("utf-8")))


consumer.subscribe(["my-stock-data"])

bucket_name="stockdata2190"
s3 = boto3.client(
    "s3",
    endpoint_url=os.environ.get("endpoint_url"),
    aws_access_key_id=os.environ.get("aws_key"),
    aws_secret_access_key=os.environ.get("aws_sec_key")
)

NO_MESSAGE_TIMEOUT = 30  # seconds
last_message_time = time.time()

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            # no message
            if time.time() - last_message_time > NO_MESSAGE_TIMEOUT:
                print("No new messages")

                partitions = consumer.assignment()
                end_offsets = consumer.get_watermark_offsets(partitions[0], timeout=5)[1]
                position = consumer.position(partitions)[0].offset

                lag = end_offsets - position
                print(f"Lag: {lag}")

                if lag <= 0:
                    print("All messages consumed.")
                    break
            continue

        if msg.error():
            print(msg.error())
            continue

        # Process message
        print(f"Consumed: {msg.value().decode('utf-8')}")
        record = msg.value()
        record = json.loads(record.decode("utf-8"))
        symbol=record.get("symbol", "unknown")
        ts = record.get("fetched_at",int(time.time()))
        key = f"{symbol}/{ts}.json"
        s3.put_object(
                Bucket=bucket_name,
                Key=key,
                Body=json.dumps(record),
                ContentType="application/json"
            )
        print(f"Saved record for {symbol}")
        consumer.commit(msg)
        last_message_time = time.time()

except Exception as e:
    print(e)
    sys.exit(1)

finally:
    consumer.close()
   

   
                    



