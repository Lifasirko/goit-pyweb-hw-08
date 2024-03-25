import pika
from models import Contact


def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    contact = Contact.objects(id=contact_id).first()
    if contact and not contact.message_sent:
        print(f"Імітуємо відправку SMS до {contact.phone_number}")
        contact.update(set__message_sent=True)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='sms')

channel.basic_consume(queue='sms', on_message_callback=callback, auto_ack=True)

print(' [*] Чекаємо на SMS-повідомлення. Для виходу натисніть CTRL+C')
channel.start_consuming()
