#seu peixe pesazado em numeiro real separa "." nao usar virgula
#pedir input do peso

p = float(input('Digite o peso do peixe'))


#sitema de decisao para saber qual resultado mostrar.
if p <= 50:
    print('Seu peixe  pesa', p,"Kg")
    print('voce nao foi tributado')
else:
    pm = p - 50
    pm = pm *4
    print('voce foi foi tributado')
    print('o valor foi de  R$',pm)

