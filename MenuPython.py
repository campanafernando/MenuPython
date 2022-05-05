#MENU MATEMÁTICO UTILIZANDO PYTHON!
from time import sleep
print('Bem vindo ao menu matemático, abaixo você terá algumas opções:')
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
opção = 0
while opção != 5:
    print('''Digite: 
    [1] para somar 
    [2] para multiplicar 
    [3] para saber qual o maior número 
    [4] para uma nova lista
    [5] para finalizar:\n''')
    opção = int(input('Qual sua opção?'))
    if opção == 1:
        res1 = n1+n2
        print(f'A soma entre {n1} e {n2} é: {res1}')
    elif opção == 2:
        res2 = n1*n2
        print(f'A multiplicação entre {n1} e {n2} é {res2}')
    elif opção == 3:
        if n1>n2:
            print(f'O número {n1} é o maior.')
        elif n2>n1:
            print(f'O número {n2} é o maior')
        else:
            print('São números iguais!')
    elif opção == 4:
        print('Informe os números novamente:\n')
        n1 = int(input('Informe o primeiro número: \n'))
        n2 = int(input('Informe o segundo número: \n'))
    elif opção == 5:
        print('Finalizando o programa...')
        sleep(2)