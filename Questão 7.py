def main():

    palavra = []
    
    for i in range(0,5):
        palavra.append(str(input("Digite uma palavra: ")))

    maior=str(max(palavra, key=len))
    print("A maior palavra digitada foi:", maior)
   
if __name__ == "__main__":
    main()