valor = int(input('Insira um valor:'))

print('%i' % valor)  # 576
ajuda = 0

cem = valor//100
ajuda = cem*100
valor = valor-ajuda

cinquenta = valor//50
ajuda = cinquenta*50
valor = valor-ajuda

vinte = valor//20
ajuda = vinte*20
valor = valor-ajuda

# fazendo
dez = valor//10
ajuda = dez*10
valor = valor-ajuda

cinco = valor//5
ajuda = cinco*5
valor = valor-ajuda

dois = valor//2
ajuda = dois*2
valor = valor-ajuda

um = valor//1
ajuda = um*1
valor = valor-ajuda




print('%i nota(s) de R$100,00' % cem)
print('%i nota(s) de R$50,00' % cinquenta)
print('%i nota(s) de R$20,00' % vinte)
print('%i nota(s) de R$10,00' % dez)
print('%i nota(s) de R$5,00' % cinco)
print('%i nota(s) de R$2,00' % dois)
print('%i nota(s) de R$2,00' % um)
