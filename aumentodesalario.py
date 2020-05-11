# entradas com o preço
salario = float(input('qual salario do funcionario ? R$'))

#calcular resultado
aumento = salario *15/100
preco = salario + aumento
#mostrar resultado
print('R${:.2f} recebeu um almento de 15% é agora você vai levar por R${:.2f}'.format(salario, aumento))