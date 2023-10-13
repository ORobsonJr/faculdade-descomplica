"""
Escreva um algoritmo que solicite ao usuário 5 números e calcula a 
multiplicação destes números digitados pelo usuário (utilize a 
estrutura de repetição for)

Escreva um algoritmo que solicite ao usuário 5 números e calcula a
multiplicação destes números digitados pelo usuário (utilize a 
estrutura de repetição while)
"""

def for_algorithm(number_list: list):
    #Example 1
    all_values = number_list

    base_number = 1

    for n in all_values:
        base_number *= n

    return base_number


def while_algorithm(number_list: list):
    #Example 2
    x = 0

    all_values = number_list

    base_number = 1

    while x < len(all_values):
        base_number *= all_values[x]
        x += 1

    return base_number


if __name__ == '__main__':
    values_list = []

    for n in range(0, 5):
        values_list.append(int(input('Digitei um número: ')))

    
    print('Pelo for: ', for_algorithm(values_list))
    print('Pelo: ', while_algorithm(values_list))