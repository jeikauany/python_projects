arquivoss = open ('Aula006/pessoas.txt', 'a') #abre o arquivo no formato de escrita colocando o conteúdo no final do arquivo
arquivoss.write('Davi\n')# insere um texto com quebra de linha 
arquivoss.close()#fecha o arquivo 

arquivi = open (Aula006/'pessoa.txt' , 'r') #abre o formato de leitura 
for linha in arquivoss:
    linha = Linha.strip()
    dados = Linha.split(';')