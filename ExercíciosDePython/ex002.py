# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

print('Faça seu cadastro: ')
nome_usuario= str(input('Digite seu nome de usuário: '))
senha_usuario= str(input('digite sua senha: '))

while nome_usuario == senha_usuario:
	print("ERRO: o usuário não pode ser igual a senha, tente novamente")
	nome_usuario=str(input("usuário: "))
	senha_usuario=str(input("senha: "))
 
print('Senha cadastrada com Sucesso! ')    