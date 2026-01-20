

contact_Schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "email", "contact", "company"],
        "properties": {
            "name": {
                "bsonType": "string",
                "description": "Name must be a string"
            },
            "email": {
                "bsonType": "string",
                "pattern": "^.+@.+\\..+$",
                "description": "Email must be a valid email format"
            },
            "contact": {
                "bsonType": "string",
                "pattern": "^[0-9]{10}$",
                "description": "Contact must be 10 digit number"
            },
            "company": {
                "bsonType": "string",
                "description": "Company name must be a string"
            }
        }
    }
}
