# numero = input("Digita um numero: ")
# numero2 = input("Digita outro numero: ")
# print(numero == numero2)
# print(numero != numero2)
# print(numero <= numero2)
# print(numero >= numero2)
# print(numero < numero2)
# print(numero > numero2)
print("-------------------------")
print(1 < 2 and 2 < 3)
print("-------------------------")
print(1== 2 or 2 != 199)
print("-------------------------")
 
nome = input("Digite o nome do aluno: ")
nota = int(input(f"Digite a nota do {nome}:"))
if nota >7:
    print(f"O {nome} foi aprovado")
    
elif nota > 4 < 7:
    print(f"O {nome} está de recuperação")
    print("Estude mais")
    
else:
    print(f"O {nome} foi reprovado")
    
print("-------------------------")
