# entrada com nome e nos 1 e 2

nome = input('Qual nome do aluno ? ')
nota1 = float(input('Qual a primeira nota ?'))
nota2 = float(input('qual a segunda nota ?'))

#motrar a formula 
#soma = nota1 + nota2
#resultado = soma / 2

#segunda  forma correeta

resultado = (nota1 + nota2) / 2 

#mostrar resultado
print('a primeira nota foi {} a segunda Nota {} a media é {}'.format(nota1, nota2, resultado))

if resultado <= 4:
    print('O aluno(a) {} foi Reprovado ' .format(nome))
else:
    print('O aluno(a) {} foi Aprovado'. formart(nome))
    