# 5 Implemente um programa para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.

salarioAtual = float(input("Digite o valor do salário atual:\n"))
valorReajuste = float(input("Digite o valor do reajuste:\n"))

calculoReajuste = salarioAtual * valorReajuste

novoSalario = calculoReajuste + salarioAtual

print("O valor do salário com o reajuste aplicado é de: R$", novoSalario, "reais")