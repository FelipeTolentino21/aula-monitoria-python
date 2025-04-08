espacamento = "\n---------------\n"

# Exercício 1 - Receba (input) uma base e uma altura e calcule/mostre a área de um triângulo
b = 10
h = 5

print("\nCálculo da área de um triângulo, o cálculo será feito da seguinte forma:")
print("Area = Base * Altura")
print(f"Exemplo, se a base valer {b} e a altura valer {h} o resultado seria {b*h}\nCom isso:")

b = int(input("Digite um valor inteiro para a base: "))
h = int(input("Digite um valor inteiro para a altura: "))

print(f"O valor da área de {b}*{h} = {b*h}")

print(espacamento)

# Exercício 2 - Crie um programa que receba um nome, imprima ele e múltiplique ele por um número recebido

nome = input("Digite um nome: ")
valor = int(input("Digite um valor inteiro: "))

nome += " "
print(f"Seja bem vindo ao Python {nome}\n{nome*valor}")

print(espacamento)

""" 
Exercício 3 - Receba (input) um valor em real (R$) e mostre a conversão para dólar americano e euro, 
mostrar o resultado em até 2 casas decimais
"""

dolar = 5.91
euro = 6.47

real = float(input("Digite um valor em reais para receber sua correspondencia em dólar e euro\nValor: "))
print(f"Valor em Reais: R$ {real:.2f}\nValor em Dólar: $ {real/dolar:.2f}\nValor em Euro: € {real/euro:.2f}")

print(espacamento)


""" 
Exercício 4 - Crie um programa que receba dois valores float, um de altura e outro de peso, 
para calcular o IMC, mostrar o resultado em até 2 casa decimais.
"""
print("Calculadora de IMC")

peso = float(input("Quanto de peso: "))
altura = float(input("Quanto de altura: "))

print(f"O seu IMC é {(peso)/(altura**2):.2f}")

print(espacamento)

""" 
Exercício 5 (Para entrega) - Receba o valor de um salário e mostre o quanto deve ser depositado de 
FGTS (8% do valor salário) para este salário informado
"""

print("Calculo para sálario e FGTS")

salarioBruto = float(input("Qual o seu salario bruto: "))

fgts = salarioBruto * 0.08
salario = salarioBruto - fgts

print(f"FGTS: {fgts:.1f}\nSalário: {salario:.1f}")