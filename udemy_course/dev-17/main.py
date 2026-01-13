
class User:
    # Constructor method
    # self represents the instance of the class
    # It binds the attributes with the given arguments
    def __init__(self, user_id, username):
        # Initialize the attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("New user being created...")

    # Method to follow another user
    # self represents the instance of the class, it must be the first parameter of any method in the class
    # user represents the user to follow
    def follow(self, user):
        user.followers += 1
        self.following += 1

    # This keyword indicates an empty block
    # It will pass  to the next line of code
    # It wont throw an error
    pass

# # Creating an instance of the User class
# # This will call the constructor method
user_1 = User("001", "angela")
user_2 = User("002", "jack")

print(user_1.id)  # Accessing the id attribute of user_1
print(user_1.username)  # Accessing the username attribute of user_1

user_1.follow(user_2)  # user_1 follows user_2
print(user_1.following)  # Accessing the following attribute of user_1
print(user_2.followers)  # Accessing the followers attribute of user_2

# # Creating another instance of the User class
# user_2 = User()
# # A dynamic attribute can be added to an instance
# # Here we are adding id and username attributes to the user instance
# user_2.id ="001"
# user_2.username= "angela"

# print(user.username)



def function():
    # It will pass  to the next line of code
    pass
