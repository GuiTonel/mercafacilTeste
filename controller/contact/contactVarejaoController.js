const ContactModel = require('../../model/contactModel')

const ContactController = require('./contactController')
const DatabasePgController = require('../database/databasePgController')

class ContactVarejaoController {
    phoneVarejao = new RegExp(/[0-9]{12,13}/)

    createModel( contactsJson = [] ) {
        var contactsModel = []
        var errors = []

        contactsJson.forEach( ( contactJson, index ) => {
            if ( contactJson.name.length <= 0 ) {
                errors.push( {
                    message: 'Invalid name!',
                    index: index
                } )
            } else if ( !this.phoneVarejao.test( contactJson.cellphone ) ) {
                errors.push( {
                    message: 'Invalid cellphone!',
                    index: index
                } )
            } else {
                var contact = Object.create(ContactModel) 
                contact.name = contactJson.name
                contact.cellphone = contactJson.cellphone
    
                contactsModel.push( contact )
            }
                
        } )

        if ( errors.length > 0 ) console.log(errors)

        return contactsModel
    }

    async insertVarejaoContacts( req, res ) {
        var contacts = this.createModel( req.body.contacts )

        try {
            console.log(contacts)
            await ContactController.insertContacts( contacts, DatabasePgController.insertContact )
        } catch (err){
            console.log(err)
            return res.status(400).send({ message: 'Error in insert contacts!' })
        }
        return res.status(200).send({ message: 'Success in insert contacts!' })
    }
}

module.exports = new ContactVarejaoController