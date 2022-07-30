import os
from calculadora import *


os.system('cls')
calculou = False
while (calculou == False):
    try:
        print('='*10, 'Calculadora Apex', '='*10)
        print('''
            1 - Soma
            2 - Subtração
            3 - Multiplicação
            4 - Divisão
        ''')

        resposta = int(input('Digite uma opção: '))
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))

        match resposta:
            case 1:
                print('Você selecionou soma')
                print('Resultado: ', soma(n1, n2))
            case 2:
                print('Você selecionou  subtração')
                print('Resultado: ', subt(n1, n2))
            case 3:
                print('Você selecionou  multiplação')
                print('Resultado: ', mult(n1, n2))
            case 4:
                print('Você selecionou divisão')
                print('Resultado: ', div(n1, n2))

        calculou = True
    except Exception as e:
        print('ocorreu um erro: ', e)   
        print('tente outra vez')



