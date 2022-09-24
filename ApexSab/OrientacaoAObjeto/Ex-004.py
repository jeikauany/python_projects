
# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#   A mensagem "Reprovado", se a média for menor do que sete;
#    A mensagem "Aprovado com Distinção", se a média for i

nota1 = input('Informe a primeira nota')
nota2 = input('Informe a segunda nota')

nota = int(nota1 + nota2) /2

if nota >= 7 and nota <10:  # nota é maior que 7 e menor que 10?
    print('Aprovado')
elif nota >= 10:            # nota é maior que 10?
    print ('Aprovado com Distinção')
else:
    print ('Reprovado')



