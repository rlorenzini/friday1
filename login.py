#login_attempts() =
#increment_login_attempts() = index + 1 per input
#reset_login_attempts() = i_l_a(index) = 0
class User:
    def __init__(self,fname,lname,age,gender,height,weight):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.login_attempt = 0
    def describe_user(self):
        print(f'Hello, {self.firstname} {self.lastname}.')
        print(f'Age: {self.age}.')
        print(f'Gender: {self.gender}.')
        print(f'Height: {self.height}.')
        print(f'Weight: {self.weight}.')
    def greet_user(self):
        print(f'Hello, {self.firstname}! I hope you enjoy your stay!')
    def login_attempts(self):
        self.login_attempt = self.login_attempt + 1
        print(f"{self.login_attempt}")
    def reset_login_attempts(self):
        self.login_attempt = 0
        print(f"{self.login_attempt}")
    def increment_login_attempts(self):
        self.login_attempt = self.login_attempt + 1






user = User('Richard','Lorenzini','26','Male','5ft6in','160 pounds')
user.describe_user()
user.greet_user()
user.login_attempts()
user.reset_login_attempts()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.login_attempts()
user.reset_login_attempts()


#
