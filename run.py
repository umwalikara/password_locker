from user import User
def create_user(username,password): #creating user
    new_user=User(username,password)
    return new_user

def save_user(user): #function save user
    user.save_user() 

def del_user(user): #function to delete user
    user.delete_user



from credentials import Credential
def create_credential(accountname,username,password):#creating credential
    new_credential=Credential(accountname,username,password)
    return new_credential

def save_credential(credential): #function to save crede
    credential.save_credential

def del_credential(credential): #function to delete crede
    credential.delete_credential