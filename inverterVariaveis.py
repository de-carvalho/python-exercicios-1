# 4 
# Escreva um programa que armazene um valor de entrada em uma variável A e o outro em uma variável B. 
# A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o valor que está em A passa para B e vice-versa. 
# Ao final escrever os valors que ficaram armazenados nas variáveis.

a = input("Insira o valor para a variável a:\n")
b = input("Insira o valor para a variável b:\n")

a, b = b, a

print("O valor da variável A é:", a + "\nO Valor da variável B é:", b)