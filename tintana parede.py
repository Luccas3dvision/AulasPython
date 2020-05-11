#dimenssoes da parede
l = float(input('Qual largura da parede?'))
a = float(input('qual a altura da parde?'))

#calculo do metro quadrado
m2 = l * a

#calculo do quantidade
tinta = m2 / 2

#mostrar resultado com casas decimias
print('Você possui{}m²  vai precisar de {:.3f} tinta '.format(m2, tinta))