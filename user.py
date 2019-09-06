class User:   
    user_list = [] 
    def __init__(self,username,password):
        self.username=username
        self.password=password
        
    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def find_by_username(username,password):
        for user in username.user_list:
            if user.username==username:
                return username
