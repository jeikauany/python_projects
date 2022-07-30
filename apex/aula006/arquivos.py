#Criação e Leitura de Arquivos
# w = abre em modo de escrita,
# se o arquivo não existir cria, se existir substitui.

arquivo = open('nomes.txt', 'w')
arquivo.write('Maycon')
arquivo.close()

# x = abre em modo de escrita,
# se o arquivo não existir cria, se existir dá erro

# arquivo = open('numeros.txt', 'x')
# arquivo.write('4')
# arquivo.close()

# a = abre em modo de escrita,
# se o arquivo não existir cria, se existir adiciona dados ao final

arquivo = open('bandas.txt', 'a')
arquivo.write('PinkFloyd')
arquivo.close()
