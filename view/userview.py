from model.usermodel import UserModel

import hashlib

from getpass import *

class UserView():
    """ """
    def __init__(self):
        self.usermodel = UserModel()
        
    
    def to_log_in(self):
        pseudo = input("veuillez saisir votre pseudo")
        view=self.usermodel.log_in(pseudo)
        if view :
            print(f"bienvenue {pseudo}!")
            return True
        else :
            print("le pseudo n'existe pas !!!!")
            return False
            
            
    def new_account(self):
        """ """
        lastname = input("veuillez saisir votre nom de famille :")
        firstname = input("veuillez saisir votre prenom :")
        pseudo = input("veuillez saisir votre pseudo :")
        email = input("veuillez saisir votre email :")
        age = int(input("veullez saisir votre age :"))
        password = getpass()
        password=hashlib.sha256(password.encode()).hexdigest()
        self.usermodel.create_an_account(lastname, firstname, pseudo, email, age, password)
        
    def to_delete_an_account(self):
        """ """
        pseudo = input("veuillez saisir votre pseudo")
        self.usermodel.delete_an_account(pseudo)
    
    def to_update_an_account(self):
        """ """        
        column = input("veuillez taper un champ disponible (lastname, firstname, pseudo, email, age, password) :")
        value = input("veuillez saisir la nouvelle valeur :")
        pseudo = input("veuillez saisir votre pseudo :")
        self.usermodel.update_an_account(column,value, pseudo)
    

         
        