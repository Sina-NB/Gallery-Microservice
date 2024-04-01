import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from photos.models import Photo

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters(host='rabbitmq', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('\n======= Message received in main ========')
    type = properties.type
    obj = json.loads(body)
    print('type: ', type, '==>', 'body: ', obj)

    if type=='create':
        photo = Photo(**obj)
        photo.save()
        print('photo saved on database.\n')
    
    elif type=='update':
        photo = Photo.objects.get(id=obj['id'])
        photo.title = obj['title']
        photo.image = obj['image']
        photo.save()
        print('photo updated on database.')
    
    elif type=='destroy':
        photo = Photo.objects.get(id=int(obj))
        photo.delete()
        print('photo removed from database.')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
