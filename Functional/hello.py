def User(username):

    if len(username) <= 2:
        print('Please enter at least 3 character')
    else:
        return'Hello', username, ' , how are you'

User('somesh')
User('so')