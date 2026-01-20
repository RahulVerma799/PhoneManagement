from flask import request, jsonify
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson import ObjectId
import re

client = MongoClient("mongodb://localhost:27017/")
db = client["phonebook_db"]
contacts_collection = db["contacts"]

class ContactController:
    
    @staticmethod
    def create_contact():
        try:
            data = request.get_json()
            
            required_fields = ['name', 'email', 'contact', 'company']
            for field in required_fields:
                if field not in data:
                    return jsonify({
                        'error': f'Missing required field: {field}'
                    }), 400
            
            if not re.match(r'^[^@]+@[^@]+\.[^@]+$', data['email']):
                return jsonify({
                    'error': 'Invalid email format'
                }), 400
            
            if not re.match(r'^\d{10}$', data['contact']):
                return jsonify({
                    'error': 'Contact must be 10 digits'
                }), 400
            
            existing = contacts_collection.find_one({'email': data['email']})
            if existing:
                return jsonify({
                    'error': 'Email already exists'
                }), 409
            
            result = contacts_collection.insert_one(data)
            
            return jsonify({
                'message': 'Contact created successfully',
                'id': str(result.inserted_id)
            }), 201
            
        except PyMongoError as e:
            return jsonify({
                'error': f'Database error: {str(e)}'
            }), 500
        except Exception as e:
            return jsonify({
                'error': f'Server error: {str(e)}'
            }), 500
    
    @staticmethod
    def get_all_contacts():
        try:
            contacts = list(contacts_collection.find({}))
            
            for contact in contacts:
                contact['_id'] = str(contact['_id'])
            
            return jsonify({
                'contacts': contacts,
                'count': len(contacts)
            }), 200
            
        except PyMongoError as e:
            return jsonify({
                'error': f'Database error: {str(e)}'
            }), 500
        except Exception as e:
            return jsonify({
                'error': f'Server error: {str(e)}'
            }), 500
    
    @staticmethod
    def get_contact(contact_id):
        try:
            if not ObjectId.is_valid(contact_id):
                return jsonify({
                    'error': 'Invalid contact ID format'
                }), 400
            
            contact = contacts_collection.find_one({'_id': ObjectId(contact_id)})
            
            if not contact:
                return jsonify({
                    'error': 'Contact not found'
                }), 404
            
            contact['_id'] = str(contact['_id'])
            
            return jsonify({
                'contact': contact
            }), 200
            
        except PyMongoError as e:
            return jsonify({
                'error': f'Database error: {str(e)}'
            }), 500
        except Exception as e:
            return jsonify({
                'error': f'Server error: {str(e)}'
            }), 500
    
    @staticmethod
    def update_contact(contact_id):
        try:
            if not ObjectId.is_valid(contact_id):
                return jsonify({
                    'error': 'Invalid contact ID format'
                }), 400
            
            data = request.get_json()
            
            existing = contacts_collection.find_one({'_id': ObjectId(contact_id)})
            if not existing:
                return jsonify({
                    'error': 'Contact not found'
                }), 404
            
            if 'email' in data and data['email'] != existing['email']:
                email_exists = contacts_collection.find_one({
                    'email': data['email'],
                    '_id': {'$ne': ObjectId(contact_id)}
                })
                if email_exists:
                    return jsonify({
                        'error': 'Email already exists'
                    }), 409
            
            if 'email' in data:
                if not re.match(r'^[^@]+@[^@]+\.[^@]+$', data['email']):
                    return jsonify({
                        'error': 'Invalid email format'
                    }), 400
            
            if 'contact' in data:
                if not re.match(r'^\d{10}$', data['contact']):
                    return jsonify({
                        'error': 'Contact must be 10 digits'
                    }), 400
            
            result = contacts_collection.update_one(
                {'_id': ObjectId(contact_id)},
                {'$set': data}
            )
            
            if result.modified_count == 0:
                return jsonify({
                    'message': 'No changes made'
                }), 200
            
            return jsonify({
                'message': 'Contact updated successfully'
            }), 200
            
        except PyMongoError as e:
            return jsonify({
                'error': f'Database error: {str(e)}'
            }), 500
        except Exception as e:
            return jsonify({
                'error': f'Server error: {str(e)}'
            }), 500
    
    @staticmethod
    def delete_contact(contact_id):
        try:
            if not ObjectId.is_valid(contact_id):
                return jsonify({
                    'error': 'Invalid contact ID format'
                }), 400
            
            existing = contacts_collection.find_one({'_id': ObjectId(contact_id)})
            if not existing:
                return jsonify({
                    'error': 'Contact not found'
                }), 404
            
            result = contacts_collection.delete_one({'_id': ObjectId(contact_id)})
            
            return jsonify({
                'message': 'Contact deleted successfully'
            }), 200
            
        except PyMongoError as e:
            return jsonify({
                'error': f'Database error: {str(e)}'
            }), 500
        except Exception as e:
            return jsonify({
                'error': f'Server error: {str(e)}'
            }), 500
    
    @staticmethod
    def search_contacts():
        try:
            query = request.args.get('query', '')
            
            if not query:
                return jsonify({
                    'error': 'Search query is required'
                }), 400
            
            search_regex = {'$regex': query, '$options': 'i'}
            
            contacts = list(contacts_collection.find({
                '$or': [
                    {'name': search_regex},
                    {'email': search_regex},
                    {'company': search_regex},
                    {'contact': search_regex}
                ]
            }))
            
            for contact in contacts:
                contact['_id'] = str(contact['_id'])
            
            return jsonify({
                'contacts': contacts,
                'count': len(contacts)
            }), 200
            
        except PyMongoError as e:
            return jsonify({
                'error': f'Database error: {str(e)}'
            }), 500
        except Exception as e:
            return jsonify({
                'error': f'Server error: {str(e)}'
            }), 500