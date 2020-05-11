# faz a leitura de todos os arquivos
arquivo = open('musica.txt', 'r')
for linha in arquivo:
    print(linha)
arquivo.close()

