import pika
from models import Contact


def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    contact = Contact.objects(id=contact_id).first()
    if contact and not contact.message_sent:
        print(f"Імітуємо відправку email до {contact.email}")
        contact.update(set__message_sent=True)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='emails')

channel.basic_consume(queue='emails', on_message_callback=callback, auto_ack=True)

print(' [*] Чекаємо на email-повідомлення. Для виходу натисніть CTRL+C')
channel.start_consuming()
