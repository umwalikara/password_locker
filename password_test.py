import unittest
from user import User

class testUser(unittest.testCase):
    def setUp(self):
        self.new_user=User("kara,dian3@10") #create user object

    def test_init(self):
        self.assertEqual(self.new_user.user_name,"kara")
        self.assertEqual(self.new_user.password,"dian3@10")

    def test_save_user(self):
        self.new_user.save_user() #saving the new username
        self.assertEqual(len(User.user_list),1)
    def teardown(self):
        User.user_list=[]

    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user=User("clack","m3@10") #new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        self.new_user.save_user()
        test_user=User("clack","m3@10") #new user
        test_user.save_user()

        self.new_user.delete_user() #deleting a contact object
        self.assertEqual(len(User.user_list),1)

    def delete_user(self):
        User.user_list.remove(self)

#test to check ifwe can find a contact by username and display info
    def test_find_user_by_username(self):
        self.new_user.save_user()
        test_user=User("clack","m3@10") #new user
        test_user.save_user()

        found_user=User.test_find_by_username("clack")
        self.assertEqual(found_user.username,password)

    @classmethod
    def find_by_username(username,password):
        for user in username.user_list:
            if user.username==username:
                return username



        
if__name__== '__main__':
    unittest.main()