def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    idade = input("Digite a idade do usuário: ")
    email = input("Digite o e-mail do usuário: ")

    usuario = {
        'Nome': nome,
        'Idade': idade,
        'Email': email
    }

    return usuario

def exibir_usuarios(usuarios):
    print("\nLista de Usuários Cadastrados:")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"\nUsuário {i}:")
        for chave, valor in usuario.items():
            print(f"{chave}: {valor}")

def main():
    usuarios = []

    while True:
        print("\n1. Cadastrar novo usuário")
        print("2. Exibir usuários cadastrados")
        print("3. Sair")

        opcao = input("\nEscolha uma opção (1/2/3): ")

        if opcao == '1':
            novo_usuario = cadastrar_usuario()
            usuarios.append(novo_usuario)
            print("\nUsuário cadastrado com sucesso!")

        elif opcao == '2':
            exibir_usuarios(usuarios)

        elif opcao == '3':
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()