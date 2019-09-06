class Credential:   
    credential_list = [] 
    def __init__(self,accountname,username,password):
        self.accountname=accountname
        self.username=username
        self.password=password
        
    def save_credential(self):
        Credential.credential_list.append(self)
        
    def delete_credential(self):
        Credential.credential_list.remove(self)
    
    @classmethod
    def find_by_accountname(accountname,username,):
        for credential in accountname.credential_list:
            if credential.accountname==accountname:
                return accountname

