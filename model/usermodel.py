from model.connection import Connection

class UserModel():
    """ """
    def __init__(self):
        self.db = Connection()
        self.choice = None
    
    def log_in(self, pseudo):
        """ """
        self.db.initialize_connection()
        #self.db.cursor.execute("SELECT * FROM users WHERE pseudo ="+"'"+pseudo+"';") 
        self.db.cursor.execute("SELECT * FROM users WHERE pseudo = %s;",(pseudo,))
        view=self.db.cursor.fetchone()
        self.db.close_connection()
        return view
        
    def create_an_account(self,lastname, firstname, pseudo, email, age, password):
        """ """
        self.db.initialize_connection()
        self.db.cursor.execute("INSERT INTO users(lastname, firstname, pseudo, email, age, password) VALUES (%s, %s, %s, %s, %s, %s);",(lastname, firstname, pseudo, email, age, password))
        self.db.connection.commit() 
        self.db.close_connection() 
        
    def delete_an_account(self,pseudo):
        """ """
        self.db.initialize_connection()
        self.db.cursor.execute("DELETE FROM users WHERE pseudo = %s;",(pseudo,))
        self.db.connection.commit()
        self.db.close_connection()
    
    def update_an_account(self,column,value, pseudo):
        """ """
        self.db.initialize_connection()
        self.db.cursor.execute("UPDATE users set "+column+" = %s WHERE pseudo = %s;",(value, pseudo,))
        self.db.connection.commit()
        self.db.close_connection()  
    
