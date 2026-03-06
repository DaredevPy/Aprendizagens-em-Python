
class Animal:
    def fazer_som(self):
        print("Som de animal")
class Mamifero(Animal):
    pass
    
class Cachorro(Mamifero):
    pass
    
    
class Gato(Mamifero):  
    def fazer_som(self):  
       print("Miau")

gato = Gato()
gato.fazer_som() # Som de animal

Cachorro = Cachorro()
Cachorro.fazer_som() # Som de animal