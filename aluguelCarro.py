# 7
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário
# Assim como a quantidade de dias pelos quais o carro foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

valorDiaria = 60
valorKM = 0.15
diasAlugados = int(input("Digite o número de dias que o veículo foi alugado:\n"))
kmRodado = float(input("Digite quantos kms o carro percorreu:\n"))

kmFinal = kmRodado * 0.15

valorFinal = (diasAlugados * valorDiaria) + kmRodado

print(f"O veículo foi alugado por {diasAlugados} dias, e percorreu {kmRodado} kilometrôs. O valor final a ser pago é de: R$ {valorFinal} reais")