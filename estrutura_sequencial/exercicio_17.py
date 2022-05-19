"""Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
quantidades de tinta a serem latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,
00. Informe ao usuário as compradas e os respectivos preços em 3 situações: comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros; misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. """

tamanho_mtr_qudr = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros = tamanho_mtr_qudr / 6.0
latas = int(litros / 18.0)
galoes = int(litros / 3.6)

if litros % 18 != 0:
    latas += 1
preco_01 = latas * 80

if litros % 3.6 != 0:
    galoes += 1
preco_02 = galoes * 25

mistura_lata = int(litros / 18)
mistura_galao = int((litros - (mistura_lata * 18)) / 3.6)

if litros - (mistura_lata * 18) % 3.6 != 0:
    mistura_galao += 1

print("Apenas latas de 18 litros: %d" % latas, "preço: %d" % preco_01)
print("Apenas galões de 3.6 litros: %d" % galoes, "preço: %d" % preco_02)
print("Mistura: %d latas e %d galoes = %.2f" % (
    mistura_lata, mistura_galao, ((mistura_lata * 80) + (mistura_galao * 25))))
