# abrir e ler misica
musica = open('musica.txt','r')
print('primeiro texto')
print(musica.read())

#seek

musica.seek(0)

# segundo texr
print('lendo linha por vez')
print(musica.readline())
print(musica.readline())


#seguinda forma linhas

print('lendo mas linhas')
print(musica.readlines())


#fexa o programa
musica.close()
