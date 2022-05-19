"""Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

temperatura = int(input("Informe a temperatura em graus Fahrenheit: "))
graus_celsius = (temperatura - 32) * 5 / 9
print("A temperatura em graus celsius é: ", graus_celsius)
