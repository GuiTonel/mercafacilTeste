const { Client } = require('pg')
const fs = require('fs')

const client = new Client({
    user: 'postgres',
    host: '127.0.0.1',
    port: '5432',
    database: 'varejao',
    password: 'wclwjq17'
})

class DatabasePgController {
    constructor(){
        try{
            client.connect()

        } catch( err ) {
            console.error(err)
        }
    }

    async createDatabaseTables(){
        return await client.query(fs.readFileSync('sql/create-table-varejao.sql').toString(), (err, res)=>{
            if (err) throw err

            console.log(res)
        })
    }

    async insertContact( contact = {} ){
        console.log('c')
        return client.query(fs.readFileSync('sql/insert-contact.sql').toString(), [ contact.name, contact.cellphone ], ( err, res ) => {
            if (err) throw err

            console.log('Success in insert contact!')
        } )
    }
}

module.exports = new DatabasePgController