#contro F no python
#abriri o aquirvio misica
print('Pesquisar palavras em linha')
arq = open('musica.txt','r')

#varivel contador
contador = 0
#funcção para encontrar linha 
for linha in arq:
    linha = linha.rstrip()
    if 'Negro' in linha:
        contador = contador + 1
        print(linha)
print('seu resultado é ',contador,'linhas')

#feixa programa
arq.close() 