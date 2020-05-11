#calcular tempo de dowload 

doc = int(input('Qual tamanho do arquivo ?'))
vel = int(input('qual a velociade da internet?'))

#mostrar resultado 

print('seu documento é de ',doc,'megabyte'  )
print('seua velocidade media é ',vel, 'mbps' )
#calculo 

vel  =  doc / 60
#  formula é velocidade =  a distancia divida por tempo que é 60 segudos

#mostrar resultado dos calculos

print('sua seu dowload sera feito em ',vel,'segundos')