"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas: Para homens: (72.7*h) - 58 Para mulheres: (62.1*h) - 44.7 """

h = float(input("Informe a sua altura: "))
peso_ide_h = (72.7 * h) - 58
peso_ide_m = (62.1 * h) - 44.7
print("O peso ideal para um homen com essa altura é:", peso_ide_h)
print("O peso ideal para uma mulher com essa altura é:", peso_ide_m)

