from view.userview import UserView

if __name__ == "__main__":
    
    userview = UserView()
    choice=input("taper a pour cree un compte ou c pour se connecter ")
    if choice == "a":
        userview.new_account()
    
    if choice == "c":
        userview.to_log_in()
        print("vous etes connecté")
        conchoice = input("que voulez vous faire tapez m pour modifier s pour supprimer q pour se deconnecter ")
        if conchoice =="m":
            userview.to_update_an_account() 
        if conchoice =="s":
            userview.to_delete_an_account() 
        if conchoice =="q":
            exit()