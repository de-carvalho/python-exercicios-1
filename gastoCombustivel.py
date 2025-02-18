# 6
# Implemente um programa para ler o preço do litro de combustível de um carro 
# ler o desempenho do veículo (km/l) e a distância entre duas cidades (km)
# e informar quantos litros, e quanto dinheiro vai ser gasto para fazer uma viagem entre as duas cidades.

precoLitro = float(input("Digite o valor do litro de combustível:\n"))
desempenhoVeiculo = float(input("Digite quantos kms o veículo faz com 1 litro:\n"))
distancia = float(input("Digite a distância em km entre as cidades:\n"))

litrosNecessarios = round(distancia / desempenhoVeiculo, 2)

gastoGasolina = litrosNecessarios * precoLitro

print("Para percorrer a distância de Garça até Marília, serão necessários", litrosNecessarios, "litros de combustível\n")
print("O valor a ser pago de combutível será de: R$", gastoGasolina, "reais")