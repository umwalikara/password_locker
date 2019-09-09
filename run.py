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

            




# if__name__=='__main__':
#     main()