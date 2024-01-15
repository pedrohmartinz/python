from tuplasEdicionarios.Funcoes.dicionarios02 import *

usuarios={}
opcao=perguntar()
while opcao == "I" or opcao == "P" or opcao == "E":
    if opcao=="I":
        inserir(usuarios)
    elif opcao=="P":
        pesquisar(usuarios,input("Qual login deseja pesquisar? "))
    elif opcao == "E":
        excluir(usuarios,input("Qual login deseja excluir? "))
    elif opcao == "L":
        listar(usuarios)
    else:
        print("Saindo do programa")
    opcao = perguntar()