# # # # def boas_vindas():
# # # #     print("Seja bem vindo")
# # # # boas_vindas()

# # # # def vindas (nomes):
# # # #     print(f"Bem vindos {nomes} na Ctrl+Play")
# # # # vindas('Akira')


# # # def titulo(cinema):
# # #     print(f"Meu filme favorito é {cinema}")
    
# # # titulo('Miranha')


# # def nome_completo (primeiro_nome , segundo_nome):
# #     print(f"Seu nome é {primeiro_nome + segundo_nome}")

# # nome_completo('akira')


# def menor (a,b):
#     if a <= b:
#         return a 
#     else:
#         return b
    
# a = 1
# b = 4

# print(f" { a }  { b }")


def preparo_do_acai (*ingredientes , tamanho="Grande"): 
    print(f"\n preparando um açai {tamanho} e com os seguintes ingredientes: ")
    
    for ingrediente in ingredientes:
        print("-" , ingrediente)
    
while True:
    preparo_do_acai(input("digite os ingredientes: ")) 
    
    if len (preparo_do_acai) != 5:
        break
    
    
    
# def dobra (lencol , gaveta) :
#     if lencol < gaveta:
#         return 0
#     else:
#         return 1 + dobra(lencol/2, gaveta)
# print(dobra(200,25))