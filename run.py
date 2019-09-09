#!/usr/bin/env python3.6
from user import User
def create_user(username, password):
    new_user = User(username,password)
    return new_user

def save_user(user): #function save user
    user.save_user() 

def del_user(user): #function to delete user
    user.delete_user

def find_user(username): #function that  finding user
    return User.find_by_username(username)

def check_existing_user(username):#Function that check if a contact exists with that user

    return User.user_exist(username)

def display_user(): #function that return all the save user
    return User.display_user()



from credentials import Credential
def create_credential(accountname,username,password):#creating credential
    new_credential=Credential(accountname,username,password)
    return new_credential

def save_credential(credential): #function to save crede
    credential.save_credential

def del_credential(credential): #function to delete crede
    credential.delete_credential

def find_credential(accountname): #function that finding credential
    return Credential.find_by_accountname(accountname)

def check_existing_credential(accountname): #Function that check if a contact exists with that accountname
    return Credential.credential_exist(accountname)

def display_credential(): #Function that returns all the saved contacts
    return Credential.display_credential()

def main():
    print("Hello, Welcome to your Password_lock. What is your name")
    username=input()
    print(f"Hello{username}.what would you like to do?")
    print('\n')

    while True:
        print("use these short codes:cc-create a new password, dc-display password, fd-find password, ex-exit the password list")
        short_code=input().lower()

        if short_code=="cc":
            print("username")
            username=input()
            print("password")
            password=input()

            print("congratirations{username}you have created a new account.")
            print('\n')
            print("enter username")
            username=input()
            print("enter password")
            password=input()

        while username!=username or password!=password:
            print("you entered wrong username or password")
            print("username")
            username=input()
            print("your password")
            password=input()

        else:
            print(f"welcome:{username} to your Account")
            print('\n')

        while True:
            print("v: view your saved credentials")
            print("c: create new credential")
            print("d: delete credential")
            print("l: log out")

            if option =='c':
                while True:
                    print("enter accountname")
                    accountname=input()
                    print("enter password")
                    print("to generate a random password, enter 'gp' or to create password, enter 'cc' ")
                    keyword=input().lower()
                    if keyword=="gp":
                        password=random.randit(22222,22222)
                        print(f"account: {accountname}")
                        print(f"username: {username}")
                        print(f"password: {password}")
                        print('\n')

                    elif keyword=='cc':
                        print("create your password")
                        accountname=input()
                        print(f"account{accountname}")
                        print(f"username{username}")
                        print(f"password{password}")
                        print('\n')

                    else:
                        print("please enter a valid code")
                        new_credential(new_credential(accountname, username, password))
                    # elif choise=='n':
                    #     break
            # if
                    





if __name__=='__main__':
    main()