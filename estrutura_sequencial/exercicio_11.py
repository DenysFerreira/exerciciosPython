"""Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""
numero_01int = int(input("Informe um número inteiro: "))
numero_02int = int(input("Informe outro número inteiro: "))
numero_03real = float(input("informe um numero real: "))

numero_01int_01 = numero_01int * 2 + numero_02int / 2
numero_01int_02 = numero_01int * 3 + numero_02int
numero_03real_03 = numero_03real * numero_03real * numero_03real

print("O produto do dobro do primeiro com metade do segundo é: ", numero_01int_01)
print("A soma do triplo do primeiro com o terceiro é: ", numero_01int)
print("O produto do terceiro elevado ao cubo é: ", numero_03real_03)
