class Restaurant:

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

        
    def describe_restaurant(self):
        full_description = f"The {self.rest_name} restaurant serves excellent {self.food_type} dishes!"
        print(full_description)
        
class IceCreamStand(Restaurant):
    def __init__(self, rest_name, food_type):
        super().__init__(rest_name, food_type)
        self.flavors = []
    
    def describe_flavors(self):
        print(f"This stand features the flavors: {self.flavors}")

rest1 = Restaurant("Fuzzy's", "tacos")
rest1.describe_restaurant()

stand1 = IceCreamStand("FroYos","Frozen Yogurt")
stand1.flavors = "Vanilla","Chocolate"
stand1.describe_restaurant()
stand1.describe_flavors()
