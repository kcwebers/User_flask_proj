from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def all_users(cls):
        # declare your query for this method
        query = "SELECT * FROM friends;"
        # run the query by calling on your db
        users_from_db = connectToMySQL('first_flask').query_db(query)

        # parse through the response data and add to new list that you can return to your controller
        all_users = []
        for user in users_from_db:
            all_users.append(cls(user))

        # return new list, which will be used but controller
        return all_users

    @classmethod
    def one_user(cls, data):
        query = "SELECT * FROM friends WHERE id=%(id)s;"
        only_user = connectToMySQL('first_flask').query_db(query, data)
        return cls(only_user[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation) VALUES (%(fname)s, %(lname)s, %(occupation)s);"
        return connectToMySQL('first_flask').query_db(query, data)
        
    @classmethod
    def edit_user(cls, data):
        query = "SELECT * FROM friends WHERE id=%(id)s;"
        user_to_update = connectToMySQL('first_flask').query_db(query, data)

        return cls(user_to_update[0])

    @classmethod
    def update_user(cls, data):
        query = "UPDATE friends SET first_name=%(first_name)s, last_name=%(last_name)s, occupation=%(occupation)s WHERE id=%(id)s;"
        updated_user = connectToMySQL('first_flask').query_db(query, data)
        return updated_user