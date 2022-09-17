# Passo a passo solução

# Abrir os 6 arquivos em Excel

# Verificar se algum valor na coluna vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.00 --> Envia um SMS com o nome, mês e as vendas do vendedor

# Caso não seja maior do que 55.00 --> não fazer nada


  
  
  
  
  
          
        
# import os
# import pandas as pd

# lista_arquivos = os.listdir('C:\\Repositorios\\python_projects\\projeto_meta_de_vendas\\arquivos_vendas')
# print(f'lista de arquivos excel: {lista_arquivos}')

# for arquivo in lista_arquivos:
#     print(f'analisando arquivo {arquivo}')
    
#     arq = pd.read_excel(f'C:\\Repositorios\\python_projects\\projeto_meta_de_vendas\\arquivos_vendas\\{arquivo}')
#     vendas = arq['Vendas'].tolist()
#     # print(vendas) 
    
#     achou_arquivo = False
#     for venda in vendas:
        
#         if venda > 55000:
            
#             print(f'achou venda: {venda} em arquivo {arquivo}')
#             print('enviar sms\n')
#             achou_arquivo = True
            
#     if achou_arquivo == False:
#         print(f'nao achou venda maior que 55.000 em arquivo {arquivo}\n')