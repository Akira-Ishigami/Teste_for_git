mes = {
    1: "janeiro" ,
    2: "fevereiro" ,
    3: "março" ,
    4: "abril" ,
    5: "maio" ,
    6: "junho" ,
    7: "julho" ,
    8: "agosto" ,
    9: "setembro" ,
    10: "outubro" ,
    11: "novembro" , 
    12: "dezembro"
}

numeroMes = int(input())

if 1 <= numeroMes <= 12:
    print(mes[numeroMes])
else:
    print("Numero invalido do mês")
