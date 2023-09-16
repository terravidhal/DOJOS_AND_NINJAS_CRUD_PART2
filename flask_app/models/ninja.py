from flask_app.config.mysqlconnection import connectToMySQL


class Ninja: 
    db = "dojos_and_ninjas_new"
    def __init__( self , data ):
        self.id = data['id']
        self.firstname = data['firstname']
        self.lastname = data['lastname']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_new').query_db(query)

        ninjas_Arr = []

        for elt in results:
            ninjas_Arr.append(cls(elt))

        return ninjas_Arr

    
    @classmethod
    def create_ninja (cls, data):

        query = "INSERT INTO ninjas ( firstname , lastname , age , created_at, updated_at, dojo_id ) VALUES ( %(first_name)s , %(last_name)s , %(age)s , NOW() , NOW(), %(dojo_id)s );"

        return connectToMySQL('dojos_and_ninjas_new').query_db( query, data )


    @classmethod
    def get_ninjas_specific_dojo(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s"

        results = connectToMySQL('dojos_and_ninjas_new').query_db(query, data)

        ninja_Arr = []

        for elt in results:
            ninja_Arr.append(cls(elt))

        #print('new results:++', ninja_Arr)
        return ninja_Arr
    

    @classmethod
    def get_specific_ninja(cls, data):
        query  = "SELECT * FROM ninjas WHERE id = %(ninja_id)s;"
        results = connectToMySQL('dojos_and_ninjas_new').query_db(query, data)
       # print('new results:++', results)
        return cls(results[0])
    

    @classmethod
    def update_ninja(cls,data):
        query = """UPDATE ninjas 
                SET firstname=%(fname)s, lastname=%(lname)s, age=%(age)s , updated_at = NOW() 
                WHERE id = %(ninja_id)s;"""
        result = connectToMySQL('dojos_and_ninjas_new').query_db(query,data)
        #print('result+++:',result) 
        return result
    

    @classmethod
    def delete_ninja(cls, data):
        query  = "DELETE FROM ninjas WHERE id = %(ninja_id)s;"
        result = connectToMySQL('dojos_and_ninjas_new').query_db(query,data)
        #print('result+++:',result) 
        return result

    

    