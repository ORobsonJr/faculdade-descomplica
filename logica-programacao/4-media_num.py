"""
Escreva um algoritmo que:
Some três números.
Calcule a mêdia entre três números.
Mostre o resultado na tela da soma e da média calculada.
"""
import random

random_num = lambda: random.randint(0, 100)
numeros = [random_num(), random_num(), random_num()]

#Soma três números
soma_total = sum(numeros)

#Calcule a mêdia entre esses três números
media_num = soma_total/len(numeros)

#Mostre o resultado na tela da soma e da média calculada.
print("Resultado da soma: {}\nResultado da média: {}".format(soma_total, media_num))
