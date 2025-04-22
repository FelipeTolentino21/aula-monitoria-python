# Exercício 1
print("---- Exercício 1 ----")
""" Crie um for que imprima os números de 1 a 10 """
for i in range(1,11):
    print(i)

# Exercício 2
print("\n---- Exercício 2 ----")
""" Crie uma função que cheque se o
número recebido é par ou ímpar."""
def parimpar(x):
    if x%2 == 0:
        print("O número é par")
    else:
        print("O número é impar")

num = int(input("Digite um número = "))
parimpar(num)

# Exercício 3
print("\n---- Exercício 3 ----")
""" Crie um For que imprima todos os
elementos dentro de uma lista. """
lista = [1,2,3,4]
for x in lista:
    print(x)

# Exercício 4
print("\n---- Exercício 4 ----")
""" Crie um While que receba números do usuário
até ele digitar um par."""
num = int(input("Digite um número: "))
while num%2!=0:
    num = int(input("O número é ímpar, digite outro: "))

# Exercício 5
print("\n---- Exercício 5 ----")
""" Quantos pares e ímpares: faça uma função que receba
uma lista de números e retorne quantos pares existem lá
dentro """
def countPar(x):
    count = 0
    for i in range(len(x)):
        if x[i]%2==0:
            count+=1
    print(f"A lista tem {count} pares")

lista = [1,2,3,4,5,6]
countPar(lista)

# Exercício 6
print("\n---- Exercício 6 ----")
""" Some o primeiro e o último: Faça um código que receba
uma lista de números inteiros, ele deve mostrar qual a soma
do primeiro número da lista com o último. """
lista = [1,2,3,4,5]
x = lista[0]
y = lista[len(lista)-1]
print(f"A soma do primeiro número e do último é {x+y}")

# Exercício 7
print("\n---- Exercício 7 ----")
""" Maior: Faça um código que receba uma lista de números
inteiros, ele deve mostrar qual o maior número entre eles. """
lista = [1,2,3,5,4]
max = 0
for i in range(len(lista)):
    if max<lista[i]:
        max=lista[i]
print(f"O maior número é o {max}")

# Exercício 8
print("\n---- Exercício 8 ----")
""" Dois números: Faça um While que recebe dois números
do usuário até que o primeiro número seja menor que o
segundo. """
x = int(input("Digite um número: "))
y = int(input("Digite o segundo número: "))
while x>=y:
    if x==y:
        print("O primeiro número é igual o segundo, digite novamente.")
    else:
        print("O primeiro número é maior que o segundo, digite novamente.")
    x = int(input("Digite um número: "))
    y = int(input("Digite o segundo número: "))

# Exercício 9 ---- O meu outro do palíndromo ficou mt mais legal ta :(
print("\n---- Exercício 9 ----")
""" Desafio: Crie uma função que receba uma string, após
isso o código deve mostrar na tela se a string enviada é um
palíndromo ou não (se escreve igual de trás para frente) """
text = input("Digite uma palavra: ")
textAlt = text.lower()
textInvertido = textAlt[::-1]

if textAlt == textInvertido:
    print(f"{text} é um palíndromo")
else:
    print(f"{text} não é um palíndromo")

# Exercício 10 
print("\n---- Exercício 10 ----")
""" Crie uma função que receba uma lista,
após isso o código deve contar quantas vezes cada
elemento aparece naquela lista. """
def countNumLista(lista):
    dicionario = {}
    for num in lista:
        if num in dicionario:
            dicionario[num] += 1
        else:
            dicionario[num] = 1
    print(dicionario)

lista = [1,2,3,4,2,4,4,3]
countNumLista(lista)