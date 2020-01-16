from view.userview import UserView

if __name__ == "__main__":
    
    userview = UserView()
    choice=input("taper a pour cree un compte ou c pour se connecter ")
    if choice == "a":
        userview.new_account()
    
    if choice == "c":
        userview.to_log_in()
    

    