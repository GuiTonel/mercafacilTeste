const routes = require('express').Router()

const contactController = require('../controller/contact/contactController')
const varejaoController = require('../controller/contact/contactVarejaoController')

routes.post('/contacts', varejaoController.insertVarejaoContacts);

module.exports = routes