import os
import json
import pika
from dotenv import load_dotenv

load_dotenv()

params = pika.URLParameters(os.environ.get('RABBITMQ_SERVER_URI'))
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin',
                          body=json.dumps(body), properties=properties)
