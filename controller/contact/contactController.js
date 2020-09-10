const varejaoController = require('./contactVarejaoController')

class ContactController {

    insertContacts(contacts = [], insertFunction){
        
        console.log( 'Number of contacts: ', contacts.length )

        var error = []

        contacts.forEach( ( contact, index ) => {
            try {
                insertFunction(contact)

            } catch (err) {
                error.unshift({ error: err, index: index })
            
            }
        } )

        if (error.length > 0) {
            console.log(error)
            throw Error('Error in insert some contact!')
        }
        return console.log('Success in insert all contacts!')
    }

    // async chosseInsertContacts(req, res){
    //     varejaoController.insertVarejaoContacts(req, res)
    // }
}

module.exports = new ContactController