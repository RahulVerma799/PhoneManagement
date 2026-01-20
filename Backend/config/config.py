from pymongo import MongoClient
from pymongo.errors import CollectionInvalid
from models.contact_Schema import contact_Schema  

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["phonebook_db"]

   
    try:
        db.create_collection("contacts", validator=contact_Schema)
        print("Contacts collection created with schema")
    except CollectionInvalid:
        print("ℹContacts collection already exists")

    contacts_collection = db["contacts"]

 
    client.admin.command("ping")
    print("Database Connected Successfully")

except Exception as e:
    print("MongoDB Connection Failed:", e)
