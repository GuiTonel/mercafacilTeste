from src.error import ContactsNotFound
from src.service import clients_service

def insert_contacts( contacts_json: dict, user_id: int ):
    if not hasattr( contacts_json, 'contacts' ):
        raise ContactsNotFound( 'Contacts not found in payload' )
    
    user = clients_service.get_client_by_id( user_id )


