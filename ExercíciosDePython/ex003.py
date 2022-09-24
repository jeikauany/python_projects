# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

nome=str(input("informe um nome: "))
while ( len(nome) <=  3 ):
	nome=str(input("informe um nome: "))

#Idade: entre 0 e 150;

idade=int(input("informe a idade: "))
while ( idade > 150 or idade < 0 ):
	idade=int(input("informe a idade: "))
	
	
#Salário: maior que zero;
salario=float(input("informe um salário: "))
while ( salario < 0 ):
	salario=float(input("informe um salário: "))
	
#Sexo: 'f' ou 'm';

sexo=str(input("informe a inicial do seu sexo: "))
while  sexo !="f" and sexo!="m" :
	sexo=str(input("informe a inicial do seu sexo: "))
	
#Estado Civil: 's', 'c', 'v', 'd';

estado_civil=str(input("informe a inicial do seu estado civil: "))
while ( estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d" ):
	estado_civil=str(input("informe a inicial do seu estado civil: "))
    

    
 