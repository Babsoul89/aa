#정적메서드와클래스메서드차이.py
class Person:
    default= "아빠"
    def __init__(self):
        self.data = self.default
    @classmethod
    def class_person(cls):
        return cls()
    @staticmethod
    def static_person():
        return Person()
    
class WhatPerson(Person):
    default = "엄마"

person1 = WhatPerson.class_person()    # return 엄마
print(person1)
person2 = WhatPerson.static_person()   # return 아빠
print(person2)