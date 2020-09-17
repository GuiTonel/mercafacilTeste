const contactModel = require('../../model/contactModel')

const DatabaseController = require('../database/databaseMacapaController')

class ContactMacapaController{
    phoneMacapa = new RegExp(/[0-9]{12,13}/)
    database = DatabaseController

    createModel( contactsJson = [] ) {
        var contactsModel = []
        var errors = []

        contactsJson.forEach( ( contactJson, index ) => {
            if ( contactJson.name.length <= 0 ) {
                errors.push( {
                    message: 'Invalid name!',
                    index: index
                } )
            } else if ( this.phoneMacapa.test( contactJson.cellphone ) ) {
                errors.push( {
                    message: 'Invalid cellphone!',
                    index: index
                } )
            } else {
                contact = Object.create(contactModel)
                contact.name = contactJson.name.toUpperCase()
                contact.cellphone = this.processCellphoneNumber(contactJson.cellphone)
    
                contactsModel.push( contact )
            }
                
        } )

        console.log(errors)

        return contactsModel
    }

    processCellphoneNumber( cellphoneNumber = '' ) {
        countryCode = '+' + cellphoneNumber.substring( 0, 2 )
        ddd = cellphoneNumber.substring( 2, 4 )
        if ( cellphoneNumber.length < 13 ) {
            firstNumberPart = cellphoneNumber.substring( 4, 8 )
            secondNumberPart = cellphoneNumber.substring( 8, 12 )
        } else {
            firstNumberPart = cellphoneNumber.substring( 4, 9 )
            secondNumberPart = cellphoneNumber.substring( 9, 13 )
        }
            
        return `${ countryCode } (${ddd}) ${firstNumberPart}-${secondNumberPart}` 
    }
}

module.exports = new ContactMacapaController