nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
prioritario="NÃO"

if idade>=65:
    prioritario="SIM"

print("O paciente " + nome + " possui atendimento prioritário? " + prioritario)