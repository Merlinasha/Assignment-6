class dog:
    def __init__(self,name,age,coatcolor):
        self.name=name
        self.age=age
        self.coatcolor=coatcolor
    def description(self,name,age):
        return f"Name:{self.name}","age:{self.age}"
    def set_info(self,coatcolor):
        self.coatcolor=coatcolor
    def get_info(self):
        print("coatcolor is",self.coatcolor)

D=dog("Puppy",3,"white")
print(D.name)
print(D.age)
D.description("puppy",3)
D.set_info("white")
D.get_info()

class JackRussellTerrier(dog):
    def breed(self):
        print("the dog name is",self.name,"and its age is",self.age,"its color is",self.coatcolor)
class Bulldog(dog):
    @classmethod
    def from_type(cls,name,age,coatcolor):
        return cls(name,age,coatcolor)
    def show(self):
        print("the name is",self.name,"and age is",self.age,"plus its color is",self.coatcolor)


J=JackRussellTerrier("cutie",2,"brown")
J.breed()
B=Bulldog("blacky",1,"black")
B.show()


















