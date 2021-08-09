from src.error import ContactsNotFound
from src.service import users_service, contacts_service

def insert_contacts( contacts_json: dict, user_id: int ):
    if not contacts_json.get('contacts', None):
        raise ContactsNotFound( 'Contacts not found in payload' )
    
    user = users_service.get_client_by_id( user_id )
    contacts = contacts_service.get_contacts_model( contacts_json['contacts'], user )
    return contacts_service.insert_contacts( contacts )
