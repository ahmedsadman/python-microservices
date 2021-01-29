import os
import pika

params = pika.URLParameters(os.environ.get('RABBITMQ_SERVER_URI'))
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')
