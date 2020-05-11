#conversor
#etradas dos valores
medida = float(input('QUal a distancia ? em metros '))
#formula dos calculos
km = medida/1000
hm = medida/100
dam = medida/10
cm = medida * 100
mm = medida * 1000
#mostrar resultado
print('{}.cm '.format(km))
print('{}.mm'.format(hm))
print('{}.mm'.format(dam))
print('{}.mm'.format(cm))
print('{}.mm'.format(mm))

