"""
Escreva um algortimo que solicite ao usuário 5 nomes e 5 notas e 
calcula a média das notas da turma (armazenar em um vetor)
"""

#Here each student's grade will be organized by indexes
alunos = []
notas = []

for i in range(0, 5):
    #input block
    nome_aluno = str(input('Digite o nome do aluno: '))
    nota_aluno = int(input('    Digite a nota do aluno {}: '.format(nome_aluno)))

    #store data in lists
    alunos.append(nome_aluno)
    notas.append(nota_aluno)

    #breakline
    print('\n')


#Display students and his grades
for index, alunos_ in enumerate(alunos):
    print("O aluno {} tirou a nota '{}'".format(alunos_, notas[index]))