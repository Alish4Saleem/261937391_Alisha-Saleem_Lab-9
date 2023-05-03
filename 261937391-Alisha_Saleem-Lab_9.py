# 261937391-Alisha_Saleem-Lab_9

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class House:
    def __init__(self, address, no_of_room):
        self.address = address
        self.no_of_room = no_of_room
        self.person = [] 

    def addPerson(self, person):
        self.person.append(person)

    def removePerson(self, person):
        if person in self.person:
            self.person.remove(person)

    def display(self):
        print(self.address)
        print("No of room:",self.no_of_room)
        for i in self.person:
            print("\t",i.name, "\t", i.age, "\t", i.gender)

# Driver Code
# Person Object
Abial = Person("Abial Zafar", 21, "Male")
Sara = Person("Sara Ahmed", 20, "Female")
Alisha = Person("Alisha Saleem", 18, "Male")

#House object and composition
house =House("FCC Quarter # 22/36", 3)
house.addPerson(Abial)
house.addPerson(Sara)
house.addPerson(Alisha)

#Display detail of person in a house
house.display()

# Remove resident
house.removePerson(Alisha)

#Display detail of person in a house
house.display()