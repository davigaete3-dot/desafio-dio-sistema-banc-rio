conta = [100]
depositos_feitos = []
saques_feitos= []
conta_new = {}

def criar_nova_conta():
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    gmail = input('Digite seu Gmail: ')
    if '@' in gmail:
        conta_new[nome] = {
            
            'idade': idade,
            'gmail': gmail
        }   
        print('Nova conta criada')
        print(conta_new)
    else:
        print('gmail invalido tente novamente')

def listar_contas_criadas():
    for nome in conta_new:
        print(f'conta criadas para o usuário {nome}')
def deposito():
    valor = float (input('qual valor deseja depositar?: '))
    conta[0] += valor
    depositos_feitos.append(valor)

def saque():
    tirar = float (input('qual valor deseja sacar: '))
    if tirar>conta[0]:
        print('não é possivel sacar')
    else:
        conta[0] -= tirar
        saques_feitos.append(tirar)
def extrato():
    print('Valores que entraram na conta: ',depositos_feitos)
    print('Valores que sairam da conta: ',saques_feitos)

while True:
    
    print(f'valor que está na conta: {conta[0]:.2f}'.replace('.',','))

    print('1-depositar')
    print('2-sacar')
    print('3-extrato')
    print('4-cadastrar conta')
    print('5-lista de contas')
    print('6-sair')
    opcao=int(input('escolha uma das opções a cima: '))
    if opcao==1:
        deposito()
    elif opcao==2:
        saque()
    elif opcao==3:
        extrato()
    elif opcao==4:
        criar_nova_conta()
    elif opcao==5:
        listar_contas_criadas()
    else: 
        break









    



    

    
    

    

    
