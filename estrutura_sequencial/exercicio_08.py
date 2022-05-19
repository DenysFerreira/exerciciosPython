"""Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês."""

salario_hr = int(input("Informe quanto você ganha por hora: "))
horas_mes = int(input("Informe a quantidade de horas trabalhadas: "))
salario_mes = horas_mes * salario_hr
print("O seu salario mensal é: ", "R$", salario_mes, "reais")
