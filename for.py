# tabuda com for 
num = int(input('qual tabuada devo Mostrar'))

#contador da tabuda
ct = 1

# usando for  e range para resolver varios  print
for ct in range(1, 11):
    print('{} X {} = {}'.format(num, ct, num*ct))