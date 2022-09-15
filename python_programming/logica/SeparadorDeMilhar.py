# Mostrar numero em formato de moeda brasileira (formatação pelo Format ou usando uma biblioteca)

faturamento = 1000000000
#print(f'O faturamento foi de R$ {faturamento:,}')

# A VÍRGULA É UM SEPARADOR DE MILHAR

# print(f'O faturamento foi de R$ {faturamento:,.3f}')

# O f NO PYTHON É FLOAT -> É UM NUMERO COM CASA DECIMAL

texto_faturamento = f"{faturamento:,.2f}" .replace (",", "_") .replace (".", ",") .replace ("_", ".")
print (f"O faturmento foi de R$ {texto_faturamento}")

# NESSA LÓGICA, EU NÃO CONSIGO TROCAR PONTO POR VÍRGULA E VIRGULA POR PONTO
# .REPLACE FAZ TODAS ESSAS TROCAR QUE PRECISO:
 
# TROCA-SE TODAS AS VÍRGULAS POR UNDERLINE
# TROCAR TODOS OS PONTOS PO VÍRGULAS
# TROCAR TODOS OS UNDERLINES POR PONTO

