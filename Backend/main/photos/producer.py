import pika
import json 

class Publisher():
    def __init__(self):
        credentials = pika.PlainCredentials('guest', 'guest')
        parameters = pika.ConnectionParameters(host='rabbitmq', credentials=credentials)
        connection = pika.BlockingConnection(parameters)
        self.channel = connection.channel()

    def publish(self, message_type, body):
        properties = pika.BasicProperties(type=message_type)
        self.channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
    
    def close(self):
        self.channel.close()
    