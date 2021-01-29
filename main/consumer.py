import os
import pika
from dotenv import load_dotenv

load_dotenv()

params = pika.URLParameters(os.environ.get('RABBITMQ_SERVER_URI'))
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback)
print('Started Consuming')
channel.start_consuming()
channel.close()
