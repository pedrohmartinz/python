arquivo = open("primeiro_arquivo.txt", "r")

conteudo = arquivo.read()
        
print(conteudo)

arquivo.close()