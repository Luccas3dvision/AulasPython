# input para pedir valor da hora trabalhada !!
vh = float(input('Quanto é sua hora de seviço?'))
h = int(input('quantas horas você trabalha no mes ?'))

#calculo mensl medio 
salario = vh*h

#mostra resultados
print('seu pagamento de ve ser R$', salario, 'com base na sua  na sua hora', vh,'reais')
print('valor baseado em',h,'horas' )