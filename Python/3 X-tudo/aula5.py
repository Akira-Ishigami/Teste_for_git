x = 0

while x < 5:
    print('valor de x : ', x)
    print(' x ainda é menor que 5, vamos somar 1')
    x+=1

else:
    print('FIM!')

 #---------------------------------------------------------------------------------------
 
# while condição:
#     codigo
#     if teste1:
#       break
    
#     if teste2:
#         continue

#     else:
#         pass
    
#     código

#-----------------------------------------------------------------------------------------

soma = 0 
x = 0 

while x < 1000:
    x+=1
    if x%3==0:
        print(x)
        soma +=x
    else:
        if x%5==0:
            pass
        else:
            print('buscando...')
            continue
    
    if soma>300:
        print(soma)
        break
    
#-----------------------------------------------------------------------------------------

