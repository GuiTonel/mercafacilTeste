const Express = require('express')
const app = new Express()

const routes = require('./src/routes')
const databaseApplicationController = require('./controller/database/databaseApplicationController')

app.use(Express.json())
app.use(Express.urlencoded( { extended: true } ))

app.use(routes)

databaseApplicationController.createDatabaseTables()

app.listen(5000)
