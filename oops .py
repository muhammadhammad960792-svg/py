class kakashi:
    Name="Minato"
    grade=10
    def display(self):
        print("my name is",self.Name)
fing=kakashi()
fing.display()


class Animal:
    Specie="Tiger"
    age=1
    def details(self):
        print("I am ",self.Specie)
    def myage(self):
        print("my age is ",self.myage)
Fox=Animal()
Fox.details()
Fox.myage()

class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print("i am a",self.name)
    def myage(self):
        print("my age is",self.age)
Parrot=Animal("blue",1)
Parrot.details()
Parrot.myage()
Tiger=Animal("kurama",31)
Tiger.details()
Tiger.myage()
Lion=Animal("son Goku",35)
Lion.details()
Lion.myage()

