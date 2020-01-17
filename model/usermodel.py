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
    
    def update_an_account(self,choice,value, pseudo):
        """ """
        self.db.initialize_connection()
        if choice =="l":
            self.db.cursor.execute("UPDATE users set lastname= %s WHERE pseudo = %s;",(value, pseudo,))
        if choice =="f":
            self.db.cursor.execute("UPDATE users set firstname= %s WHERE pseudo = %s;",(value, pseudo,))
        if choice =="p":
            self.db.cursor.execute("UPDATE users set pseudo= %s WHERE pseudo = %s;",(value, pseudo,))
        if choice =="e":
            self.db.cursor.execute("UPDATE users set email= %s WHERE pseudo = %s;",(value, pseudo,))
        if choice =="a":
            self.db.cursor.execute("UPDATE users set age= %s WHERE pseudo = %s;",(value, pseudo,))
        if choice =="d":
            self.db.cursor.execute("UPDATE users set password= %s WHERE pseudo = %s;",(value, pseudo,))
        self.db.connection.commit()
        self.db.close_connection()  
    
