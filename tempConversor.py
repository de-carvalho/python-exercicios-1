# 8
#Escreva um programa para ler uma temperatura em Fahrenheit, calcular e escrever o valor correspondente em graus Celsius:
# Fórmula C = ((F - 32)/9) * 5

fahrenheit = float(input("Digite a temperatura em Fahrenheit:\n"))

celsius = round(((fahrenheit - 32) / 9) * 5, 1)

print(f"Fahrenheit: {fahrenheit}. A temperatura em Celsius é de: {celsius}")