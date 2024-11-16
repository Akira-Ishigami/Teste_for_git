num = range(1,11)
i=0

for tabu in num:
    print(f"{tabu} x {1+1} = {tabu*(i+1)}")
    i += 1
#=---------------------------------------------------------------------------------=   
valores = []
for _ in range (1,11):
    valores.append(int(input("Digite um valor inteiro: ")))
    
maior_valor = valores[0]
posição_maior = 0

