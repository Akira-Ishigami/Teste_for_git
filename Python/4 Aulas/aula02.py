# Estrutara de Dados

numero1 = 10
numero2 = 20

# ----------------------------------------------------

texto1 = "Ctrl"
texto2 = "Play"

# Igualdade

print(numero1 * 2 == texto2)
print(texto1 == texto2)

# Desigualdade

print(60 != 20)
print(texto1 != texto2)

# Maior , menor ou igual

print(numero1 > numero2)
print(numero1 >= numero2)
print(numero1 < numero2)

# And e Or

print(1 < 2 < 199)
print(1 < 2 and 2 < 199)

print(1 > 2 or 2 > 199)
print(200 < 999 or 200 > 1)

# If e Else

idade = int(input("Digite sua idade: \n")) 

if idade <= 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade")

