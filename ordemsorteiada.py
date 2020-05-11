import random
#aleatorio
alu1 = input('NOME DO ALUNO 1')
alu2 = input('NOME DO ALUNO 2')
alu3 = input('NOME DO ALUNO 3')
alu4 = input('NOME DO ALUNO 4')
#usar lista para random lista em cochete
sala = [alu1, alu2, alu3, alu4]
# escolha = random.choice(sala)
random.shuffle(sala)
#mostrar resultado
# print('O aluno foi escolhinho é {}'.format(escolha))
#mostra embaralhada
print(sala)