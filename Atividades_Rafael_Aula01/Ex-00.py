#  Crie uma aplicação que calcule o IMC do indivíduo, pesquise a fórmula e aplique.

peso = float(input('Qual seu peso?'))
 
altura = float(input("Qual a sua altura"))

imc = peso/(altura * 2)

print('Seu índice de massa corporal é {:.2f}'.format(imc)) 
