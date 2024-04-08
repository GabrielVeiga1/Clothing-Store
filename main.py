from colorama import Fore, Style
import os

# Função para limpar a tela do terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para centralizar o texto na largura da tela
def centralizar(texto):
    largura_terminal = os.get_terminal_size().columns
    espacos_laterais = (largura_terminal - len(texto)) // 2
    return " " * espacos_laterais + texto

# Definição da classe Produto
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

# Função para exibir os produtos disponíveis
def exibir_produtos(produtos):
    clear_screen()
    print("\n" + centralizar(Fore.GREEN + " "*6 + "Produtos disponíveis:" + Style.RESET_ALL) + "\n") # Ajuste de posicionamento aqui
    for i, produto in enumerate(produtos, 1):
        print(f"{i}. {produto.nome} - {Fore.YELLOW}R${produto.preco:.2f}{Style.RESET_ALL}")

# Função para adicionar produtos ao carrinho
def adicionar_ao_carrinho(carrinho, produtos):
    clear_screen()
    exibir_produtos(produtos)
    escolha = int(input("\nEscolha o número do produto que deseja adicionar ao carrinho: "))
    if escolha >= 1 and escolha <= len(produtos):
        carrinho.append(produtos[escolha - 1])
        print(centralizar("\n" + Fore.GREEN + " "*24+ "Produto adicionado ao carrinho!" + Style.RESET_ALL))
        
    else:
        print(centralizar(Fore.RED + "Escolha inválida." + Style.RESET_ALL))

# Função para exibir o carrinho
def exibir_carrinho(carrinho):
    clear_screen()
    print(centralizar(Fore.GREEN + "Seu carrinho:" + Style.RESET_ALL))
    print('')
    if not carrinho:
        print(centralizar(Fore.YELLOW + "Seu carrinho está vazio." + Style.RESET_ALL))
    else:
        for produto in carrinho:
            print(f"- {produto.nome} - {Fore.YELLOW}R${produto.preco:.2f}{Style.RESET_ALL}")

# Função para finalizar a compra
def finalizar_compra(carrinho):
    clear_screen()
    valor_total = sum(produto.preco for produto in carrinho)
    print(Fore.GREEN + f"Valor total da compra: R${valor_total:.2f}")
    print('')
    print(Fore.YELLOW + "Compra finalizada. Obrigado!" + Style.RESET_ALL)

# Função principal
def main():
    # Produtos disponíveis na loja
    produtos = [
        Produto("Camiseta", 29.99),
        Produto("Calça jeans", 49.99),
        Produto("Tênis", 79.99)
    ]

    carrinho = []

    # Loop principal do programa
    while True:
        clear_screen()
        print("\n" + centralizar(Fore.BLUE + " "*8 + "Bem-vindo à Loja Virtual!" + Style.RESET_ALL) + "\n") # Ajuste de posicionamento aqui
        print(centralizar("Opções:"))
        print(centralizar("1. Ver produtos disponíveis"))
        print(centralizar("2. Adicionar produto ao carrinho"))
        print(centralizar("3. Ver carrinho"))
        print(centralizar("4. Finalizar compra"))
        print(centralizar("5. Sair"))

        opcao = input("\n" + centralizar("Escolha uma opção: "))

        if opcao == '1':
            exibir_produtos(produtos)
            input("\n" + centralizar("Pressione Enter para continuar..."))
        elif opcao == '2':
            adicionar_ao_carrinho(carrinho, produtos)
            input("\n" + centralizar("Pressione Enter para continuar..."))
        elif opcao == '3':
            exibir_carrinho(carrinho)
            input("\n" + centralizar("Pressione Enter para continuar..."))
        elif opcao == '4':
            finalizar_compra(carrinho)
            input("\n" + centralizar("Pressione Enter para sair..."))
            break
        elif opcao == '5':
            print("\n" + centralizar(Fore.RED + "Saindo..." + Style.RESET_ALL))
            break
        else:
            print("\n" + centralizar(Fore.RED + "Opção inválida." + Style.RESET_ALL))
            input("\n" + centralizar("Pressione Enter para continuar..."))

if __name__ == "__main__":
    main()
