from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dog import Dog

class Friend:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dogs = []

##############################################
# Mapping Dogs to Friend
##############################################
    @classmethod
    def get_dogs_by_friend(cls, data):
        query = "SELECT * FROM friends JOIN dogs ON friends.id = friend_id WHERE friends.id = %(id)s;"
        results = connectToMySQL('first_flask').query_db(query, data)

        group = cls(results[0])

        for row_from_db in results:
            data = {
                "id":row_from_db['dogs.id'],
                "name":row_from_db['name'],
                "description":row_from_db['description'],
                "created_at":row_from_db['dogs.created_at'],
                "updated_at":row_from_db['dogs.updated_at'],
            }
            group.dogs.append(Dog(data))
        return group
##############################################
# Get All route
##############################################
    @classmethod
    def all_friends(cls):
        # declare your query for this method
        query = "SELECT * FROM friends;"
        # run the query by calling on your db
        friends_from_db = connectToMySQL('first_flask').query_db(query)
        # parse through the response data and add to new list that you can return to your controller
        all_friends = []
        for friend in friends_from_db:
            all_friends.append(cls(friend))
        # return new list, which will be used but controller
        return all_friends

##############################################
# Get One route
##############################################
    @classmethod
    def one_friend(cls, data):
        query = "SELECT * FROM friends WHERE id=%(id)s;"
        only_friend = connectToMySQL('first_flask').query_db(query, data)
        return cls(only_friend[0])
##############################################
# Save One (new/create) route
##############################################
    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation) VALUES (%(fname)s, %(lname)s, %(occupation)s);"
        return connectToMySQL('first_flask').query_db(query, data)
##############################################
# Update One route
##############################################
    @classmethod
    def update_friend(cls, data):
        query = "UPDATE friends SET first_name=%(first_name)s, last_name=%(last_name)s, occupation=%(occupation)s WHERE id=%(id)s;"
        updated_friend = connectToMySQL('first_flask').query_db(query, data)
        return updated_friend
##############################################
# Delete One (new/create) route
##############################################
    @classmethod
    def delete_friend(cls, data):
        query = "DELETE FROM friends WHERE id=%(id)s;"
        connectToMySQL('first_flask').query_db(query, data)