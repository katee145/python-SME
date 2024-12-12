import os 

os.system("clear")


class Bird:
    # CLASS ATTRIBUTE
    numBirds = 0

    # CONSTRUCTOR
    def __init__(self, kind, call):
        # INSTANCE VARIABLES/PROPERTIES
        self.kind = kind
        self.call = call
        Bird.numBirds += 1 #increases the class variable tracker of birds by 1 each time
        print(f"Number of birds = {Bird.numBirds}")

    # BEHAVIOUR
    def describe (self):
        return f"{self.kind} goes {self.call}."

class Big_Bird(Bird): # this is a subclass of Bird
    
    def __init__(self, kind, call, wingspan):
        self.wingspan = wingspan
        super().__init__(kind, call) #calls the Bird class

    def describe(self):
        return f"{self.kind} goes {self.call}, and has a wingspan of {self.wingspan} feet!" #this overrides the describe above for eagle

class Really_big_bird(Big_Bird): #by calling big bird you also call bird
    def __init__(self, kind, call, wingspan, age):
        self.age = age
        super().__init__(kind, call, wingspan)

    def describe(self):
        return f"{self.kind} goes {self.call}, and has a wingspan of {self.wingspan} feet! It is {self.age} years old and massive!"    


owl = Bird("Owl", "Twit Twoo") #this is an instance of the bird class
crow = Bird("Crow", "Caw")

#big bird
eagle = Big_Bird("Eagle", "Screech", 25)

vulture = Really_big_bird("Vulture", "Squawk", 60, 200) #really big bird 

print(vulture.describe())

print(eagle.describe())

print(owl.describe()) #instead of describe you could write .call or .kind to print relevant
print(crow.describe()) 