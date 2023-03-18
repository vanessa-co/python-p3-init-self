#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name 
        self.breed = breed
   
my_dog = Dog("Fido")
print(my_dog.name)
print(my_dog.breed)

my_other_dog = Dog("Skyler", breed="Golden Retriever")
print(my_other_dog.name)
print(my_other_dog.breed)
    

    #def bark(self):
        #print("Woof!")

    #def get_adopted(self,owner_name):
        #self.owner = owner_name   

#fido = Dog("Fido")
#fido.get_adopted("Sophie")
#fido.favorite_toy      

#snoopy = Dog("Snoopy", "Tennis Ball")
#snoopy.favorite_toy

