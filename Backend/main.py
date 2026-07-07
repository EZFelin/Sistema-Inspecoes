from usuarios import buscar_usuario_por_nome, cadastrar_usuario, listar_usuarios
from equipamentos import cadastrar_equipamento, listar_equipamentos

while True:

    print("\n===== Sistema de Inspeções =====")
    print("1 - Cadastrar equipamento")
    print("2 - Listar equipamentos")
    print("3 - Cadastrar usuário")
    print("4 - Listar usuários")
    print("5 - Buscar usuário por nome")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_equipamento()

    elif opcao == "2":
        listar_equipamentos()

    elif opcao == "3":
        cadastrar_usuario()

    elif opcao == "4":
        listar_usuarios()
    
    elif opcao == "5":
        nome = input("Digite o nome do usuário: ")
        buscar_usuario_por_nome(nome)

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")