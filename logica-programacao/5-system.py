"""
Escreva um algoritmo em python que solicite ao usuário três números:
- Some três números informados pelo usuários
- Calcule a média entre três números.
- Mostre o resultado na tela da soma e da média calculada.
"""

#Input data
number_list = []

while len(number_list) < 3:
    number_list.append(float(input('Digite um número: ')))


#Process data
soma = round(sum(number_list), 2)
average = round(soma/len(number_list), 2)

#Output data
print("O resultado da soma é: {}\nO resultado da média calculada é: {}".format(soma, average))