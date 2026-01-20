
from flask import Blueprint
from controllers.contact_controller import ContactController


contact_bp = Blueprint('contact_bp', __name__)

@contact_bp.route('/contacts', methods=['POST'])
def create():
    return ContactController.create_contact()

@contact_bp.route('/contacts', methods=['GET'])
def get_all():
    return ContactController.get_all_contacts()




@contact_bp.route('/contacts/<contact_id>', methods=['PUT'])
def update(contact_id):
    return ContactController.update_contact(contact_id)

@contact_bp.route('/contacts/<contact_id>', methods=['DELETE'])
def delete(contact_id):
    return ContactController.delete_contact(contact_id)