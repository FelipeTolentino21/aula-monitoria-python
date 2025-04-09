# Exercício 1 - Calculadoa
""""
print("-- Calculadora --")
print("Digite qual operação deseja realizar\n1- Soma\n2- Subtração\n3- Divisão\n4- Multiplicação")
aux = int(input("Escolha: "))
print("")
print("Insira dois numeros")
x = float(input("Número 1: "))
y = float(input("Número 2: "))
print("")
if aux==1:
    print(f"Resultado: {x+y}")
elif aux==2:
    print(f"Resultado: {x-y}")
elif aux==3:
    print(f"Resultado: {x/y}")
else:
    print(f"Resultado: {x*y}")
"""
# Execício 2 - Avaliação de notas
"""
print("--- Avaliação de notas ---")
nota1 = float(input("Insira a nota 1: "))
nota2 = float(input("Insira a nota 2: "))
nota3 = float(input("Insira a nota 3: "))
"""
# Jeito que o Guilherme fez na aula
"""
if nota1>=5 or nota2 >=5 or nota3>=5:
    print("Aprovado!")
else:
    print("Reprovado!")
"""
# Jeito que o exercício pediu
"""
if nota1>=5:
    print("Aprovado!")
else:
    print("Reprovado!")

if nota2>=5:
    print("Aprovado!")
else:
    print("Reprovado!")

if nota3>=5:
    print("Aprovado!")
else:
    print("Reprovado!")
"""
# Exercício 3 - Programa que retorna a hora que for digitada de acordo com o horário
hora = int(input("Que horas são: "))
if  hora>= 0 and hora < 6:
    print(f"Agora são {hora} horas. Boa Madrugada.")
elif hora >= 6 and hora < 12:
    print(f"Agora são {hora} horas. Bom Dia.")
elif hora >= 12 and hora < 18:
    print(f"Agora são {hora} horas. Boa Tarde.")
elif hora >= 18 and hora < 24:
    print(f"Agora são {hora} horas. Boa Noite.")
else:
    print("Horário inválido")