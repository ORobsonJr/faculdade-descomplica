"""
Escreva um algoritmo que solicite ao usuário dois números e verifique 
se o primeiro número digitado é maior que o segundo número digitado,
se verdadeira escreva a frase "O Primeiro número é o maior", senão
escreva a frase "O segundo número é o maior".
"""

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

#maior_num return the largest number and his index
maior_num = lambda lista_n: [max(lista_n), lista_n.index(max(lista_n))]

#we'll use it as support to define the largest value
valores_complementares = ['primeiro', 'segundo']

values_function = maior_num([num1, num2])

print("O maior número é o {} e o seu valor é {}".format(
    valores_complementares[values_function[1]]),
    values_function[0]
    )