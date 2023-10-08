class SistemaEventos:
    def __init__(self):
        self.tabela_hash = {}

    def função_hash(self, categoria):
        return hash(categoria) % 10  # Usando uma função hash simples com tamanho fixo

    def inserir_evento(self, nome, categoria):
        índice = self.função_hash(categoria)
        if índice not in self.tabela_hash:
            self.tabela_hash[índice] = []
        self.tabela_hash[índice].append((nome, categoria))

    def remover_evento(self, nome, categoria):
        índice = self.função_hash(categoria)
        if índice in self.tabela_hash:
            self.tabela_hash[índice] = [(n, c) for n, c in self.tabela_hash[índice] if n != nome]
    def mostrar_eventos_por_categoria(self, categoria):
        índice = self.função_hash(categoria)
        eventos_categoria = self.tabela_hash.get(índice, None)

        if eventos_categoria is None:
            print("Categoria não encontrada.")
        else:
            print(f"Eventos na categoria '{categoria}':")
            for evento in eventos_categoria:
                print("-", evento[0])
    def buscar_por_categoria(self, categoria):
        índice = self.função_hash(categoria)
        eventos_categoria = [evento[0] for evento in self.tabela_hash.get(índice, []) if evento[1] == categoria]
        return eventos_categoria

    def listar_categorias(self):
        categorias = set(evento[1] for lista_eventos in self.tabela_hash.values() for evento in lista_eventos)
        return list(categorias)

# Função para exibir o menu e lidar com a entrada do usuário
def menu():
    sistema = SistemaEventos()
    while True:
        print("\nMenu:")
        print("1. Adicionar Evento")
        print("2. Listar Categorias")
        print("3. Mostrar Eventos por Categoria")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do evento: ")
            categoria = input("Digite a categoria do evento: ")
            sistema.inserir_evento(nome, categoria)
            print("Evento adicionado com sucesso!")

        elif escolha == "2":
            categorias = sistema.listar_categorias()
            print("\nCategorias disponíveis:")
            for categoria in categorias:
                print("-", categoria)

        elif escolha == "3":
            categoria = input("Digite a categoria para mostrar os eventos: ")
            sistema.mostrar_eventos_por_categoria(categoria)

        elif escolha == "4":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
