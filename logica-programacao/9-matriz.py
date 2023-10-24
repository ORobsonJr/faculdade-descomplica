"""
Com base no exemplo anterior, desenvolva um algoritmo que some cada 
valor de uma posição da matriz com 2. Mostre o resultado na tela.
Dica1: soma=soma + 2
Dica2: Use mais dois laços para mostrar na tela o resultado.
"""

import random

#Generate a list with 5 random values
generate_random_list = lambda: random.sample(range(1, 99), 5)
matriz_sum = 2

#Generate a matriz of 5 rows and 5 columns
vetor_base = [
    generate_random_list(),
    generate_random_list(),
    generate_random_list(),
    generate_random_list(),
    generate_random_list()
]

for index, n1 in enumerate(vetor_base):
    print('Valores somados com 2 da lista ',index)
    for n2 in n1:
        print("    Valor original: {}, valor somado: {}".format(n2, n2+matriz_sum))

