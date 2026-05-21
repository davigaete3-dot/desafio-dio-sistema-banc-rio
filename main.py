conta = [100]
depositos_feitos = []
saques_feitos= []

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
    print('4-sair')
    opcao=int(input('escolha uma das opções a cima: '))
    if opcao==1:
        deposito()
    elif opcao==2:
        saque()
    elif opcao==3:
        extrato()
    else: 
        break








    



    

    
    

    

    