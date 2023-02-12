class Bank:
    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance
        
    def display(self):
        print("name : " + self.name +"\nbalance : "+ str(self.balance))

    def withdraw(self, amount):
        # self.balance = self.balance - amount
        self.balance -= amount 

    def deposit(self, amount):
        # self.balance = self.balance + amount
        self.balance += amount


b1 = Bank()
b1.set_details("NDB")
b2 = Bank()
b2.set_details("CDB")

b1.display()
b1.deposit(1000)
b1.display()
b1.withdraw(100)
b1.display()