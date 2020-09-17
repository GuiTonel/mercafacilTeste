const UserModel = {
    name: {
        type: String,
        required: true
    },
    password: {
        type: String,
        required: true,
        select: false
    }
}

module.exports = UserModel