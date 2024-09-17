class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, gender={self.gender})"
# Instantiate the class
person1 = Person(name='John', age=21, gender='male')
print(person1)