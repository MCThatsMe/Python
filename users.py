class User:
    def __init__(self, first_name, last_name, username, age, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.login_attempts = login_attempts
    
    def describe_user(self):
        user_description = f"\nThis peron's full name is {self.first_name} {self.last_name}. \n"
        user_description += f"The username they chose is {self.username} and they are {self.age} years old. \n"
        user_description += f"They have logged in {self.login_attempts} times."
        print(user_description)
        
    def greet_user(self):
        greeting = f"\nWelcome, {self.username}. Let's get started."
        print(greeting)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Administrator(User):
    def __init__(self, first_name, last_name, username, age, login_attempts=0):
        super().__init__(first_name, last_name, username, age, login_attempts=0)
        self.privileges = []
    
    def show_privileges(self):
        print(f"The Administrator has the following permissions: ")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")

user1 = User("Michael", "Cullison", "cullisonmj", 30)

User.greet_user(user1)
user1.increment_login_attempts()
User.describe_user(user1)

admin1 = Administrator("Joe", "Mama", "jomama", 31)

admin1.privileges = ("can add post", "can delete post", "can ban users")
#Administrator.greet_user(admin1)
#Administrator.describe_user(admin1)
#Administrator.show_privileges(admin1)

admin1.show_privileges()