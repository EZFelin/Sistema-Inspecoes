from Backend.conexao import conectar
from Backend.usuarios import cadastrar_usuario, listar_usuarios

print("1 - Cadastrar usuário")
print("2 - Listar usuários")

opcao = input("Escolha: ")

if opcao == "1":
    cadastrar_usuario()
elif opcao == "2":
    listar_usuarios()