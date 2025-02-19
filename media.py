# 2 Fazer um programa para receber 3 valores inteiros do usário e mostrar a sua média

num1 = int(input("Insira o primeiro número:\n"))
num2 = int(input("Insira o segundo número:\n"))
num3 = int(input("Insira o terceiro número:\n"))

med = (num1 + num2 + num3) / 3

print("A média dos valores é de", round(med, 2))