from abc import ABC, abstractmethod


class Person(ABC):
    #abstract method
    def get_gender(self):
        pass

    

class Male(Person):
    #overriding abstract method
    def get_gender(self):
        print("Male")



class Female(Person):
    #overriding abstract method
    def get_gender(self):
        print("Female")


#driving code
male=Male()
male.get_gender()


female=Female()
female.get_gender()
        
