from flask_app.config.mysqlconnection import connectToMySQL


class Dojo: 
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_new').query_db(query)
        # print("results :", results)
        dojos_Arr = []

        for elt in results:
            dojos_Arr.append(cls(elt))

        return dojos_Arr

    
    @classmethod
    def create_dojo(cls, data):
        
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"

        return connectToMySQL('dojos_and_ninjas_new').query_db( query, data )


    @classmethod
    def get_specific_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(dojo_id)s"

        results = connectToMySQL('dojos_and_ninjas_new').query_db(query, data)

        #print('new results:++', cls(results[0]))
        return cls(results[0])


        
 