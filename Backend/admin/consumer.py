import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from photos.models import Photo

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(host='rabbitmq', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('\n======= Message received in admin ========')
    type = properties.type
    obj = json.loads(body)
    print('type: ', type, '==>', 'body: ', obj)
    
    if type=='update':
        photo = Photo.objects.get(id=obj['id'])
        photo.likes = obj['likes']
        photo.save()
        print('photo updated on database.')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
