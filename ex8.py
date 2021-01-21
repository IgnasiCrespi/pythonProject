def main():
    x=int(input("introdueix un número "))
    y=int(input("introdueix un número "))
    z=int(input("introdueix un número "))
    
    resultat1=x+y+z
    print("El resultat de la suma dels tres números és: ",resultat1)
    
    if x==y and x==z and y==z:
        resultat2=x+y+z
        resultat3=resultat2*3
        print("El resultat és: ", resultat3)
if __name__ == "__main__":
    main()