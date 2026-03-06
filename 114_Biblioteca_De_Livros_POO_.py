class Livro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    
class Biblioteca:
    def __init__(self):
        self.livros = []
    
    def adicionar_livros(self,livro):
        self.livros.append(livro)
        pass
    
    def mostrar_livros(self):
        if self.livros:
            print("Livros na Biblioteca:")
            for livro in self.livros:
                print(livro.titulo, "-", livro.autor)
        else:
            print("A biblioteca está vazia.")   
Livro_1 = Livro("Dom Casmurro","Machado de Assis")
Livro_2 = Livro("O Pequeno Príncipe","Antoine de Saint-Exupéry")   

Biblioteca = Biblioteca()
Biblioteca.adicionar_livros(Livro_1)
Biblioteca.adicionar_livros(Livro_2)      

Biblioteca.mostrar_livros()        