const { Client } = require('pg')
const fs = require('fs')

const client = new Client({
    user: 'postgres',
    host: '127.0.0.1',
    port: '5432',
    database: 'varejao',
    password: 'wclwjq17'
})

class DatabaseApplicationController {
    constructor(){
        try{
            client.connect()

        } catch( err ) {
            console.error(err)
        }
    }

    async createDatabaseTables(){
        return await client.query(fs.readFileSync('sql/create-table-user.sql').toString(), (err, res)=>{
            if (err) throw err

            console.log(res)
        })
    }

    async insertUser( user ){
        return await client.query(fs.readFileSync('sql/insert-user.sql').toString(), [user.name, user.password], (err, res)=>{
            if (err) throw err

            console.log(res)
        })
    }

    async selectUsers(){
        var rows = await client.query(fs.readFileSync('sql/select-user.sql').toString()).then( ( res ) => {
            return res.rows
        } )

        return(rows)
    }
}

module.exports = new DatabaseApplicationController