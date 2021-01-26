import pika

params = pika.URLParameters(
    'amqps://qvkgfrcb:fzsy9w8pJ_m1ir_MZWdxtkoI-45Q4GGS@rattlesnake.rmq.cloudamqp.com/qvkgfrcb')
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
