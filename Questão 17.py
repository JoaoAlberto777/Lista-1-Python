def main():

    Numeros = []
    SomaImpar = 0

    for i in range(0,5):
        Numeros.append(int(input("Digite um número: ")))

    for i in Numeros:
        if i % 2 == 0:
            SomaImpar += i
    print("A soma dos números ímapres: ",SomaImpar)    

if __name__ == "__main__":
    main()