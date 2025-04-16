def palindromo(palavra):
    flag=True
    letras = 0
    palavraMinuscula = palavra.lower()
    for i in palavraMinuscula:
        letras+=1

    if letras%2==0:     # Caso seja par
        # Coisa que checa se é palindromo
        for i in range(0, (letras//2)-1):
            if palavraMinuscula[i] == palavraMinuscula[letras-i]:
                continue
            else:
                flag=False
                break

    else:               # Caso seja impar
        # Remove letra do meio
        letraMeio = (letras//2)
        palavraSemLetraMeio = palavraMinuscula[:letraMeio] + palavraMinuscula [letraMeio+1:]

        letras=0
        for i in palavraSemLetraMeio:
            letras+=1
        print(letras)
        print(palavraSemLetraMeio)
        # Coisa que checa se é palindromo
        for i in range(0, (letras//2)-1):
            print(i)
            if palavraSemLetraMeio[i] == palavraSemLetraMeio[letras - i - 1]:
                continue
            else:
                flag=False
                break
    
    if flag == True:
        print("É Palindromo")
    else:
        print("Não é palindromo")

palavra = input("Texto: ")

palindromo(palavra)