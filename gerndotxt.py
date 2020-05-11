# criando arquivo¨¨
arquivo = open('arq01.txt','w')
arquivo.write('Lucas  \n')
arquivo.write('entre o sucesso\n')
arquivo.write('e a \n')
arquivo.write('lama\n')
arquivo.close()

#lendo arquivo criado
arquivo = open('arq01.txt','r')
for linha in arquivo:
    linha = linha.rstrip()
    print(linha)
arquivo.close()