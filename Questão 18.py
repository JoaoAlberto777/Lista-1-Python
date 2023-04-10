def main():

    Numeros = []
    Produto = 1

    for i in range(0,5):
        Numeros.append(int(input("Digite um número: ")))
        Produto = Produto * Numeros[i]
    
    print("O produto desses números é: ",Produto)
if __name__ == "__main__" :
    main()