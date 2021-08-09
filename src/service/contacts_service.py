from src.database.schemas import User
from src.service import users_service 


def insert_contacts( contacts: list ):
    [ contact.save() for contact in contacts ]
    return {"Succecss": "Contacts inserted sucessfully"}

def get_contacts_model( contacts_list: list, user: User ):
    user_schema = users_service.get_contact_user_type( user )
    contacts_model_list = [ user_schema.to_model( nome=contact["name"], celular=contact["cellphone"] ) for contact in contacts_list ]
    return contacts_model_list