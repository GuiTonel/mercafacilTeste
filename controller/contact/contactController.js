const varejaoController = require('./contactVarejaoController')
const macapaController = require('./contactMacapaController')

class ContactController {
    
    async insertContacts(req, res){
        var controller = chosseControllerById()



        try {
            await insertContacts( controller.createModel(req.body.contacts), controller.database.insertContact )

        } catch (err){
            console.log(err)
            return res.status(400).send({ message: 'Error in insert contacts!' })
            
        }
        return res.status(200).send({ message: 'Success in insert contacts!' })
    }
}

function chosseControllerById( userId ) {
    var userName = 'varejao'

    switch (userName.toUpperCase()){
        case 'VAREJAO':
            return varejaoController
        case 'MACAPA':
            return macapaController
    }
}

    
async function insertContacts(contacts = [], insertFunction){
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

module.exports = new ContactController