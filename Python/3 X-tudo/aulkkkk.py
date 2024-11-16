for _ in range(6):
    def preparo_do_acai (*ingredientes , tamanho = "Grande"):
        print(f"\n preparando um açai {tamanho} e com os seguintes ingredientes: ")
        
        for ingrediente in ingredientes:
            print("-" , ingrediente)
            
    preparo_do_acai(input("digite os ingredientes: "))
    