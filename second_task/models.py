from mongoengine import Document, StringField, BooleanField, connect

from mongoengine import connect
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

# connect to cluster on AtlasDB with connection string

connect(host=f"mongodb+srv://{mongo_user}:{mongodb_pass}@clustertest.s6h4lrj.mongodb.net/?retryWrites=true&w=majority&appName=ClusterTest", ssl=True)



class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    message_sent = BooleanField(default=False)
    phone_number = StringField(required=False)  # Додаткове поле
    preferred_method = StringField(required=False)  # SMS або email
