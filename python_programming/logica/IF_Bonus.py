# IF NA MESMA LINHA PARA SITUAÇÕES SIMPLES

# SE O FUNCIONÁRIO VENDEU MAIS DO QUE R$ 500,00 O BÔNUS É DE R$ 200,00
# SE O FUNCIONÁRIO VENDEU MENOS DO QUE R$ 500,00 O BÔNUS É DE R$ 50,00

#faturamento = 1000  # aqui eu digo quanto ele vendeu

#if faturamento > 500:
#    bonus = 200
#else:
#    bonus = 50
#print (bonus)

# POSSO TRANSFORMAR ESSE IF ACIMA EM UMA ÚNICA LINHA DE CÓDIGO, DA SEGUINTE FORMA:

faturamento = 1000

bonus = 200 if faturamento > 500 else 50

print(bonus)