#inputs com nome e nota
aluno = input('Qual nome do aluno')
n1 = float(input('qual nota á 1'))
n2 = float(input('qual nota á 2'))
n3 = float(input('qual nota á 3'))
n4 = float(input('qual nota á 4'))

#formula de calculo

nx = n1 + n2 + n3 + n4 
media = nx / 4

#mostrar resultado media 

print('a media do(a) é',aluno,'sua media é', media )

#acrssentando if else

if  media <= 4:
    print('aluno reprovado')
else:
    print('aluno Passou')
