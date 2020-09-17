const ContactModel = require('../../model/contactModel')

const DatabaseController = require('../database/databaseVarejaoController')

class ContactVarejaoController {
    phoneVarejao = new RegExp(/[0-9]{12,13}/)
    database = DatabaseController

    createModel(contactsJson = []) {
        var contactsModel = []
        var errors = []

        contactsJson.forEach((contactJson, index) => {
            if (contactJson.name.length <= 0) {
                errors.push({
                    message: 'Invalid name!',
                    index: index
                })
            } else if (!this.phoneVarejao.test(contactJson.cellphone)) {
                errors.push({
                    message: 'Invalid cellphone!',
                    index: index
                })
            } else {
                var contact = Object.create(ContactModel)
                contact.name = contactJson.name
                contact.cellphone = contactJson.cellphone

                contactsModel.push(contact)
            }

        })

        if (errors.length > 0) console.log(errors)

        return contactsModel
    }

}

module.exports = new ContactVarejaoController