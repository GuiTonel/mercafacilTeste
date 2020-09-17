const routes = require('express').Router()

const contactController = require('../controller/contact/contactController')
const userController = require('../controller/user/userController')

//Contatos
routes.post('/contacts', contactController.insertContacts);

//Usuarios
routes.post( '/user', userController.registerUser )
routes.get('/user', userController.getUsers)

module.exports = routes