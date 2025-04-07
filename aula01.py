fruta = "pera"
print(f"banana {fruta} maca") 
""" O 'f' é usado para formatar, ou seja, conseguir inserir a variável 'fruta' no meio da string. 
Por padrão o Python adiciona uma quebra de linha no final da string """
print(type(fruta)) # Função para mostrar o tipo da variável

x = 20
y = 3

print(x/y) # Faz conversão implícida de variáveis
print(x//y) # É usado para retornar apenas o valor inteiro

a = "banana"
b = "maca"

print(a+b) # Concatenação de strings
print(a*2) # Operação com strings

nome = input("Digite seu nome: ")

numero = int(input("Digite um numero: ")) # É necessário fazer a conversão explícita para trocar o tipo. Também é possível fazer "numero = int(numero)" para converer

print("Seu nome é", nome)
print("Seu numero é", numero)

print("O tipo do seu nome é", type(nome))
print("O tipo do seu número é", type(numero))

caracter = "g"
print("O valor do " + caracter + " na tabela ASCII é", ord(caracter)) # 'ord' é uma "função" que ordena a variável caracter para o número 103, que é o seu valor na tabela ASCII