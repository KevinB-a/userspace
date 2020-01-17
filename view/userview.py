from model.usermodel import UserModel

class UserView():
    """ """
    def __init__(self):
        self.usermodel = UserModel()
    
    def to_log_in(self):
        pseudo = input("veuillez saisir votre pseudo")
        self.usermodel.log_in(pseudo)
    
    def new_account(self):
        """ """
        lastname = input("veuillez saisir votre nom de famille :")
        firstname = input("veuillez saisir votre prenom :")
        pseudo = input("veuillez saisir votre pseudo :")
        email = input("veuillez saisir votre email :")
        age = int(input("veullez saisir votre age :"))
        password = input("veuillez saisir votre mot de passe :")
        self.usermodel.create_an_account(lastname, firstname, pseudo, email, age, password)
        
    def to_delete_an_account(self):
        """ """
        pseudo = input("veuillez saisir votre pseudo")
        self.usermodel.delete_an_account(pseudo)
    
    def to_update_an_account(self):
        """ """        
        choice = input("choisir la colonne a modifier l pour lastname f pour firstname p pour pseudo e pour email a pour age et d pour password")
        value = input("veuillez saisir la nouvelle valeur")
        pseudo = input("veuillez saisir votre pseudo")
        self.usermodel.update_an_account(choice,value, pseudo)