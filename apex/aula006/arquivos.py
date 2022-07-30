#Criação e Leitura de Arquivos
# w = abre em modo de escrita,
# se o arquivo não existir cria, se existir substitui.

arquivo = open('nomes.txt', 'w')
arquivo.write('Maycon')
arquivo.close()