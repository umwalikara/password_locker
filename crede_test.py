import unittest
from credentials import Credential

class testCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential=Credential("pinterest","kara","dian3@10") #create crede object
    
    def test_init(self):
        self.assertEqual(self.new_credential.accountname,"pinterest")
        self.assertEqual(self.new_credential.username,"kara")
        self.assertEqual(self.new_credential.password,"dian3@10")

    def test_save_credential(self):
        self.new_credential.save_credential() #saving the new credential
        self.assertEqual(len(Credential.credential_list),1)

    def tearDown(self):
        Credential.credential_list=[]

    def test_save_multiple_credential(self):
        self.new_credential.save_credential()
        test_credential=Credential("pinterest","clack","m3@10") #new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
        self.new_credential.save_credential()
        test_credential=Credential("pinterest","clack","m3@10") #new credential
        test_credential.save_credential()

        self.new_credential.delete_credential() #deleting a credential object
        self.assertEqual(len(Credential.credential_list),1)

#test to check if we can find a credential by accountname and display info
    def test_find_credential_by_accountname(self):
        self.new_credential.save_credential()
        test_credential=Credential("pinterest","clack","m3@10") #new credential
        test_credential.save_credential()

        found_credential=Credential.find_by_accountname("pinterest")
        # self.assertEqual(found_credential.accountname,test_credential.accountname)


if __name__=='__main__':
    unittest.main()