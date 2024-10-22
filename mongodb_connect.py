from pymongo import MongoClient
import ssl
import certifi

def connect_to_mongodb(uri: str):
    try:
        # إنشاء عميل MongoDB مع SSL
        client = MongoClient(uri, ssl=True, ssl_cert_reqs=ssl.CERT_REQUIRED, tlsCAFile=certifi.where())
        
        # اختبار الاتصال
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        
        return client
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        return None

# استبدل ب URI الخاص بك
mongodb_uri = "mongodb+srv://apptmvipbot:wV9KQkaySlqNvfQk@cluster0.y1yqp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# الاتصال بقاعدة البيانات
db_client = connect_to_mongodb(mongodb_uri)
