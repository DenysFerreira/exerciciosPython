"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidade de latas de tinta a serem compradas e o
preço total. """

tamanho_mtr_qudr = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros = tamanho_mtr_qudr / 3.0
latas = int(litros / 18.0)
if litros % 18 != 0:
    latas += 1

print("A quantidade de latas de tinta a serem compradas é:", latas, "latas")
print("O preço total das latas de tinta é:", "R$", latas * 80, "reais")
