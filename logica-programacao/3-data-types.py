"""
Classifique os dados de acordo com seu tipo independente do algortimo,
caso seja um literal conte seu tamanho e caso seja real diga quantas casas
decimais possui, para inteiros e reais verifique se é negativo ou positivo:

"Eu gosto de programar"
123976.0
1.3849
""
"nome"
0
"@##$%"
"""

dados = ["Eu gosto de programar", 123976.0, 1.3849, "", "nome", 0, "@##$%"]

for d in dados:
    if type(d) is str:
        print("O dado '{}' é um literal e possui {} caracteres".format(d, len(d)))

    elif type(d) is float or int:
        real_negativo = lambda num: "negativo" if num <= 0 else "positivo"

        if type(d) is float:
            contar_decimal = lambda dado: len(str(dado).split('.')[1])
            print("O dado '{}' é um real {} e possui {} casas decimais".format(d, real_negativo(d) ,contar_decimal(d)))
        
        else:
            print("O dado '{}' é um inteiro {}".format(d, real_negativo(d)))


