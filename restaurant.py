#restaurant class with two props
#1. describe_restaurant() prints 2 info
#2. open_restaurant() prints message indicating open

class Restaurant:
    def __init__(self,title,serve):
        self.title = title
        self.serve = serve

    def describe_restaurant(self):
        print(f"We are {self.title} and we serve {self.serve}!!!")

    def open_restaurant(self):
        print("We are open for business!!!")

tacos = Restaurant('Loco Tacos', 'Mexican Food')
tacos.describe_restaurant()
tacos.open_restaurant()
burgers = Restaurant('BurgerFi', 'Burgers and Fries')
burgers.describe_restaurant()
burgers.open_restaurant()

#call d_r() three more times
nachos = Restaurant('Nacho Cheese', 'Nachos')
nachos.describe_restaurant()
salads = Restaurant('Lettuce Feed You', 'Salad Bar')
salads.describe_restaurant()
fastfood = Restaurant('Quick Serve', 'anything you want, but fast')
fastfood.describe_restaurant()

#create superclass user with first_name, last_name, and several other properties
#describe_user() = user's info printed; greet_user() = personalized greeting message

class User:
    def __init__(self,fname,lname,age,gender,height,weight):
        self.firstname = fname
        self.lastname = lname
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
    def describe_user(self):
        print(f'Hello, {self.firstname} {self.lastname}.')
        print(f'Age: {self.age}.')
        print(f'Gender: {self.gender}.')
        print(f'Height: {self.height}.')
        print(f'Weight: {self.weight}.')
    def greet_user(self):
        print(f'Hello, {self.firstname}! I hope you enjoy your stay!')

user = User('Richard','Lorenzini','26','Male','5ft6in','160 pounds')
user.describe_user()
user.greet_user()




#
