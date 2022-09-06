def DizerOi(msg):
    if 'sim' in msg:
        print('Olá')
    
def PedirIdade(idade):
    if idade > 18:
        print('maior de idade')
    else:
        print('menor de idade')
    
def DizerAdeus(resposta):
    res = ''
    if 's' in resposta:
        res = 's'
        print('Adeus')
    else:
        print('vamos outra vez')
        
    return 's'
    
def main():
    
    res = ''
    while res != 's':
        oi = 'sim'
        DizerOi(oi)
        
        tentar = True
        while tentar == True:
            
            try:
                idade = int(input('digite a idade'))
                if type(idade) == int:
                    PedirIdade(idade)
                tentar = False
            except:
                print('tente novamente')
        
        res = input('deseja sair? (s == sim - n == nao): ')
        DizerAdeus(res)
        
main()