const Express = require('express')
const app = new Express()

const routes = require('./src/routes')
const databasePgController = require('./controller/database/databasePgController')

app.use(Express.json())
app.use(Express.urlencoded( { extended: true } ))

app.use(routes)

databasePgController.createDatabaseTables()

app.listen(5000)
