from flask_app.config.mysqlconnection import connectToMySQL

class Dog:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['first_name']
        self.description = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

##############################################
# Save One (new/create) route
##############################################
    @classmethod
    def save_dog(cls, data):
        query = "INSERT INTO dogs (name, description, occupation, created_at) VALUES (%(name)s, %(description)s, NOW());"
        return connectToMySQL('first_flask').query_db(query, data)
