inventario=[]
resposta = "S"
while resposta == "S":
    equipamento=[input("Equipamento: "),
                 float(input("Valor: ")),
                 int(input("Número Serial: ")),
                 input("Departamento: ")]
    inventario.append(equipamento)
    resposta = input("Digite \"S\"para continuar: ").upper()

valores=[]
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print("O item mais caro custa: ", max(valores))
    print("O item mais barato custa: ", min(valores))
    print("O total é de: ", sum(valores))