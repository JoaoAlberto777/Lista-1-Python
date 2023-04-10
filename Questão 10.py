def main():

    Soma = 0
    Media = 0
    Tam = 0
    
    for i in range(0,5):
        numero=(int(input("Digite um número: ")))
        Soma += numero
        Tam += 1
    Media = Soma / Tam
    print("A média dos números é: ", Media)

if __name__ == "__main__" :
    main()