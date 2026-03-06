
class Cachorro:
    #Atributos 'variaveis'
    
    def __init__(self,nome,raça,idade): #__init___ é o construtor da classe, ele é chamado quando a classe é instanciada
        #self é uma referencia a própria classe, ou seja, a instancia que foi criada
        self.nome = nome
        self.raça = raça
        self.idade = idade
    
    def latir(self):
        print(F"O Cachorro {self.nome} esta latindo")
    
    #Metodos (funções/Ações)
    
class Gatos:
    pass
#Isntanciando Classe

    toto = Cachorro ("Toto","Sem raça",8)
    #caramelo  = Cachorro ("Caramelo","Sem raça",5)
    toto.latir()
    