const UserModel = require('../../model/userModel')
const Bcrypt = require('bcryptjs')

const DatabaseController = require('../database/databaseApplicationController')

class UserController{

    async registerUser(req, res){
        var user = await createUserModel(req.body)

        try{
            await DatabaseController.insertUser( user )

            user.password = undefined

            return res.status(200).send({ user })
        } catch (err){
            return res.status(400).send({ error: 'Falha ao registrar usuario!' })
        }
    }

    async getUsers( req, res ){
        var users = await DatabaseController.selectUsers()

        res.send({users})
    }
}

async function createUserModel( bodyUser ) {
    var { name } = bodyUser
    var { password } = bodyUser

    user = Object.create(UserModel)
    user.name = name
    const hash = await Bcrypt.hash( password, 10 )
    user.password = hash

    return user
}

module.exports = new UserController