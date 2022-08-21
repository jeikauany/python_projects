def salvar(nome):
    with open('apex/aula007/pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome}\n')

def listar():
    nomes = []
    with open('apex/aula007/pessoas.txt', 'r') as arquivo:
        for l in arquivo:
            l = l.strip()
            nomes.append(l)
    return nomes         

salvar('Jei')
print(listar())