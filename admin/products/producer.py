#
import pika

params = pika.URLParameters(
    'amqps://qvkgfrcb:fzsy9w8pJ_m1ir_MZWdxtkoI-45Q4GGS@rattlesnake.rmq.cloudamqp.com/qvkgfrcb')
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')
