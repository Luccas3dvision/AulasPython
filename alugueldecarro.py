#entrada de variaveis 

km = float(input('Quantos kilometos percorrido?'))
dia = int(input('Quantos dias ficou com carro ?'))

#fomula de calculo
dias = dia
total = (km * 0.15) + (dias * 60) 
#formula do resultado
print('Voce alugou o carro por {:.2f} Dias e andou {:.2f}km com ele dando um total de R${}'.format(dia, km, total))