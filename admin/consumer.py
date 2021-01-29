import os
import pika
from dotenv import load_dotenv

load_dotenv()

params = pika.URLParameters(os.environ.get('RABBITMQ_SERVER_URI'))
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(
    queue='admin', on_message_callback=callback, auto_ack=True)
print('Started Consuming')
channel.start_consuming()
channel.close()
