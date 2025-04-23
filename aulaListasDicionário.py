produtos = ["uva", "banana", "maca", "pera"]
escolha = 0
while escolha != -1:
    print(f"Sua lista de compras tem os seguintes produtos: {produtos}")
    print("Deseja:\n1 - Adicionar um produto\n2 - Remover um produto pelo nome\n3 - Remover um produto pela sua posição na lista\n4 - Quantos produtos desse tem na lista\n5 - Substituir um produto na lista")
    escolha = int(input("Escolha (-1 para sair): "))

    if escolha == -1:
        continue

    elif escolha == 1:
        adc = input("Digite qual produto quer adicionar: ")
        produtos.append(adc)

    elif escolha == 2:
        flag = False
        rem = input("Digite qual produto quer remover: ")
        while flag == False:
            if rem not in produtos:
                print("O produto que você digitou não está na lista, tente novamente!")
                rem = input("Digite qual produto quer remover: ")
                continue
            for i in range(len(produtos)):
                if rem == produtos[i]:
                    produtos.remove(rem)
                    flag = True
                    print(f'O produto {rem} foi removido com sucesso!')
                    break
        continue   

    elif escolha == 3:
        flag = False
        prod = int(input("Digite qual a posição do produto que quer remover: "))
        while flag == False:
            if prod > len(produtos) or prod <= 0:
                print("A posição que você selecionou não está na lista, tente novamente!")
                prod = int(input("Digite qual a posição do produto que quer remover: "))
                continue
            else:
                produtos.pop(prod-1)
                flag = True
                print(f'O produto na posição {prod} da lista foi removido com sucesso!')  
        continue   

    elif escolha == 4:
        flag = False
        pos = input("Digite qual produto quer saber a quantidade: ")
        while flag == False:
            if pos not in produtos:
                print("O produto que você digitou não está na lista, tente novamente!")
                pos = input("Digite qual produto quer saber a quantidade: ")
                continue
            else:
                flag = True
                print(f'O produto "{pos}" aparece na lista {produtos.count(pos)} vezes')
        continue   

    elif escolha == 5:
        flag = False
        prod = int(input("Digite qual a posição do produto que quer substituir: "))
        while flag == False:
            if prod > len(produtos) or prod <= 0:
                print("A posição que você selecionou não está na lista, tente novamente!")
                prod = int(input("Digite qual a posição do produto que quer substituir: "))
                continue
            else:
                flag=True
                novoProd = input(f"Qual o produto quer trocar por {produtos[(prod-1)]}: ")
                produtos.insert((prod-1), novoProd)
        continue  

    else:
        print("A escolha que você selecionou não existe")
        print("Deseja:\n1 - Adicionar um produto\n2 - Remover um produto pelo nome\n3 - Remover um produto pela sua posição na lista\n4 - Saber em que posição o produto está na lista\n5 - Substituir um produto na lista")
        escolha = int(input("Escolha (-1 para sair): "))
        continue
print("Obrigado por este programa! Até mais!")