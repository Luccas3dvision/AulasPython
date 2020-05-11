#contador de linhas python

contador = 0 
arq = open('musica.txt', 'r')
for linha in arq:
    contador = contador + 1
print('numeros de linhas:', contador)
arq.close()
