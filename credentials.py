class Credential:   
    credential_list = [] 
    def __init__(self,accountname,username,password):
        self.accountname=accountname
        self.username=username
        self.password=password
        
    def save_credential(self):
        Credential.credential_list.append(self)