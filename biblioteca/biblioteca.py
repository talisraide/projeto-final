from livro.livro_fisico import LivroFisico


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.socios = []

    def adicionarLivro(self, livro: LivroFisico):
        self.livros.append(livro)
        print("Livro adicionado com sucesso!")

    def removerLivro(self, id_livro):
        for livro in self.livros:
            if livro.id == id_livro:
                self.livros.remove(livro)
                return True
        return False

    def listarLivros(self):
        for livro in self.livros:
            print(livro)
