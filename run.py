from user import User
def create_user(username,password):
    new_user=User(username,password)
    return new_user

from credentials import Credential
def create_credential(accountname,username,password):
    new_credential=Credential(accountname,username,password)
    return new_credential
