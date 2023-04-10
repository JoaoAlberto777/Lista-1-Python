def main():

    Numeros = []

    for i in range(0,5):
        Numeros.append(int(input("Digite um número: ")))

    print("Aqui está os números em ordem Decrescente: ")

    Numeros.sort(key=int,reverse=True)

    print(Numeros, end=' ,')

if __name__ == "__main__" :
    main()