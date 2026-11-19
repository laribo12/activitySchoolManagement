#Exercise 1
class Person:
    def __init__(self,name, __age):
        self.__age = __age
        self.name = name

    def get_age(self):
        return self.__age
    
person1 = Person("LINA", 20)
person2 = Person("Jerzon", 67)
print(f"Name: {person1.name}, {person2.name}")
print(f"Age: {person1.get_age()}, {person2.get_age()}")

#IT is better to access __age by get_age becuase it allows you to control how data is accessed and modified