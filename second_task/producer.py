import pika
import faker
from models import Contact

fake = faker.Faker()

# Встановлення з'єднання з RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Створення черги, якщо вона ще не існує
channel.queue_declare(queue='emails')

for _ in range(10):  # Генерація 10 фейкових контактів
    method = "email" if fake.boolean() else "SMS"
    queue = 'emails' if method == "email" else 'sms'
    contact = Contact(
        fullname=fake.name(),
        email=fake.email(),
        phone_number=fake.phone_number(),
        preferred_method="email" if fake.boolean() else "SMS"
    )
    contact.save()

    # Відправка id контакту у чергу
    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=str(contact.id))

print(" [x] Відправлено 10 контактів")
connection.close()


# python second_task\producer.py
# python second_task\consumer.py
#
