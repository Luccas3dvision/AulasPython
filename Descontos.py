# entradas com o preço
produto = float(input('Qual o presso do produto ? R$'))

#calcular resultado
desconto = produto *10/100
preco = produto - desconto
#mostrar resultado
print('R${} recebeu um deconto de 5% é agora você vai levar por R${}'.format(produto, desconto))