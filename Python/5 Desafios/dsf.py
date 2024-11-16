Matematica = int(input("Digite a nota de matematica: \n"))

if Matematica < 5:
    print(f"O aluno tirou {Matematica} , portanto está reprovado.")
elif Matematica <= 6:
    print(f"O aluno tirou {Matematica} , portanto está em recuperação.")
else:
    print(f"O aluno tirou {Matematica} , portanto está em aprovado.")



nome = input("Escreva o nome do aluno:\n")

a = int(input(f"Digite a nota de Matematica do {nome}:\n"))
b = int(input(f"Digite a nota de Portugues {nome}:\n"))

pesoA = 7
pesoB = 6

somapesos = pesoA + pesoB

media = (a * pesoA + b * pesoB) / somapesos

print(f"A media ponderada do {nome} é {media:.2f}")




nome = input("Digite o nome do aluno:\n")
nota = int(input("Digite a nota do aluno:\n"))

if nota >= 7:
    print(f"O aluno {nome} foi Aprovado com nota {nota}")

elif nota >= 5:
    print(f"O aluno {nome} está de Recuperação com nota {nota}")
else:
    print(f"O aluno {nome} está Reprovado com nota {nota}")

