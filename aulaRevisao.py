import random

# Crie uma função que recebe uma lista de numeros e devolve a média deles
def media(lista):
    soma = 0
    quantidade = 0
    for itens in lista:
        soma += itens
        quantidade += 1
    return soma/quantidade

numeros = [2,4,6,8,10]
print(f"A média dos numeros da lista é: {media(numeros)}")

# Faça um programa que receba uma palavra e descubra quantas vogais existem na palavra
vogais = ["a", "e", "i", "o", "u"]
count = 0
palavra = input("Digite uma palavra pra saber quantas vogais tem nela: ").lower()
for letras in palavra:
    if letras in vogais:
        count += 1
print(f"Tem {count} vogais na sua palavra")

# Dado um dicionário de alunos com notas, exiba apenas os alunos com nota maior ou igual a 8
avaliacao = {
    "Joãozinho": 5,
    "Pedrinho": 6,
    "Carlinho": 7,
    "Enzinho": 8,
    "Rogerinho": 9,
    "Cristianinho": 10,
    "Chicózinho": 4,
    "Miguelzinho": 3
}

for aluno, nota in avaliacao.items():
    if nota>=8:
        print(f"Aluno {aluno} possui nota maior ou igual a 8")

# Crie um programa de sorteio. O usuário digitará 5 números de 1 a 50. Em seguida, 5 números serão sorteados, mostre os acertos.
digitados = []
sorteados = []
acertos = []

print("Digite 5 números de 1 a 50:")
for numeros in range(0,5):
    digitados.append(int(input(f"Número {numeros+1}: ")))

for numeros in range(0,5):
    sorteados.append(random.randint(1,50))

for numeros in range(0,5):
    if digitados[numeros] == sorteados[numeros]:
        acertos.append(digitados[numeros])
    else:
        acertos.append("x")

print(f"Acertos: {acertos}")