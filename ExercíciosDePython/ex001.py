# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input('Peça um número de zero a 10: '))
while nota < 0 or nota > 10:
    nota = int(input("Informe a nota: "))

    if nota < 0 or nota > 10:
        print("Valor inválido")

