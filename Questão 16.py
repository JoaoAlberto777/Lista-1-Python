def main():

    numeros = []

    SomaPares=0
    for i in range(0,5):
        numeros.append(int(input("Digite um número: ")))

    for i in numeros:
        if (i % 2 == 0):
            SomaPares += i
    print("A soma dos números pares é: ",SomaPares)    

if __name__ == "__main__" :
    main()