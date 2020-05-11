#tabuada
#entrada do valor
num = int(input('Qual Numero?'))

#formula 1
print('-----------------------')
for num2 in range(1,11):
    resultado = num*num2
    print('{:2} X {:2} = {:2} '.format(num, num2, resultado))
print('-----------------------')

#formula 2 é escrever tudo na mão