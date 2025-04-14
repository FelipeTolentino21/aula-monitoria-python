# Senha numérica

senha = 4320

tentativa = int(input("Digite a senha: "))

while tentativa != senha:
    if(tentativa>9999 or tentativa<1000):
        tentativa = int(input("A senha possui apenas 4 dígitos!\nTente Novamente:"))
    else:
        tentativa = int(input("Senha Incorreta!\nTente novamente: "))
    if(tentativa == senha):
        print("Senha correta!\nAcesso concedido")

# Senha em formato de string

senha2 = "SenhaLegau123"

tentativa2 = input("Digite a senha: ")

while tentativa2 != senha2:
    tentativa2 = input("Senha Incorreta!\nTente novamente: ")
    if(tentativa2 == senha2):
        print("Senha correta!\nAcesso concedido")