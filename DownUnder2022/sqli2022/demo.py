import os 

class Ba:
    def __init__(self, name) -> None:
        self.name = name
        
    def getName(self):
        return self.name 
    
class Me:
    def __init__(self) -> None:
        pass
class Con(Ba, Me):
    pass 

x = Con("aws")
name = "d47"
print(x.getName())
print(x.__class__.__base__)
print(x.__class__.__bases__)
print(x.__class__.__mro__)
print(x.__class__.__mro__[1].__subclasses__()[0].__init__.__globals__)
print(x.__class__.__mro__[1].__subclasses__()[0].__init__.__globals__["name"]) 
print(x.__class__.__mro__[1].__subclasses__()[0].__init__.__globals__["__builtins__"].eval("print(11111)")) 