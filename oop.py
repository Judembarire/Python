# object-oriented programing
class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


person1 = People(name="john", age=70, sex="male")

person2 = People("jowie", 45, "male")

print(f"my name is {person1.name} and i am person one and my age is {person1.age} and my sex is {person1.sex}")


# person = Person()
# person.name = "Hailey"
# print(person.name)
