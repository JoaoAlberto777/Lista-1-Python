def main():
    
    lista = [5]

    for i in range(0,5):
        lista.append(int(input("Digite um número: ")))
    maior=max(lista) 

    print("O maior número digitado foi: ", maior)
if __name__ == "__main__":
    main()
    