# Combinação e Permutação

# Programa para imprimir todas as permutações usando a
# função da biblioteca itertools

from itertools import permutations

# Obtem todas as permutações do vetor a
a = [1, 2, 3]
perm = permutations(a)

print ("Todas as permutações possíveis do vetor ", a, "são: ")
for i in list(perm):
    print(i) 

# Obtem todas as permutações do vetor a de tamanho 2
perm = permutations(a, 2)

print ("Todas as permutações possíveis de tamanho 2 do vetor ", a, "são: ")
for i in list(perm):
    print(i) 