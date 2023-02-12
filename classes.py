class Person:
    def set_details(self, name, age):
        # print("I am a person", self)
        self.name = name
        self.age = age
    
    def display(self):
        print("I am a person", self)

    def greet(self):
        if self.age < 80:
            print("Hello, how are you doing?", self)
        else:
            print("How do yo do?")
        self.display()
    
    def get_old(self):
        self.age = 75

p1 = Person()
p2 = Person()

p1.set_details("Bob", 28)
p2.set_details("marlet",90)

# p1.display()
p1.greet()

# p2.display()
p2.greet()
p1.get_old()