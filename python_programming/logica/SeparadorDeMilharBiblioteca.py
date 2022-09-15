# O PYHTON TEM UMA BIBLIOTECA PADRÃO QUE JA VEM INSTALADA, CHAMADA "LOCALE", ESSA BIBLIOTACA PERMITE VOCÊ ADAPTAR UMA SÉRIE DE COISAS AO FORMATO LOCAL
# FORMATO LOCAL: AQUI NO BRASIL USA-SE VÍRGULA PARA SEPARAR CASA DECIMAL E PONTO PARA SEPARAR O MILHAR


faturamento = 1000000000
texto_faturamento = f"{faturamento:,.2f}" .replace (",", "_") .replace (".", ",") .replace ("_", ".")
print (f"O faturmento foi de R$ {texto_faturamento}")

# SEGUE A LÓGICA PARA USO DESSA BIBLIOTECA:

from ast import Import
import locale

# 1 - DEFINIR QUAL LOCAL VC ESTÁ
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # Se esse não rodar, usar: "Portuguese_Brazil.1252"

texto_faturamento2 = locale.currency(faturamento, grouping= True) # Grouping agrupa os zeros / Caso não queira usar o cifrão usa-se: symbol= false, do contrário ele aparece no resultado
print (f"O faturmento foi de {texto_faturamento2}")


