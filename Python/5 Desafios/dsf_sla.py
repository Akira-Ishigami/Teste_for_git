dados_client = {}

nome = input("Digite o nome do cliente: ")

endereco = input("Digite o endereco: ")

cpf = input("Digite o Cpf: ")
if len(cpf) != 11:
        print("Cpf invalido")
        
tel = int(input("Digite o Telefone: "))
if len(cpf) != 10:
        print("Telefone invalido")

dados_client['nome'] = {
    'Cpf' : cpf , 
    'Telefone' : tel , 
    'Endereco' : endereco 
}

print(dados_client)