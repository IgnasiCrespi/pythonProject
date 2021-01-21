def main():
    print("NÚMERO PRIMO")
    numero = int(input("Escriba un número entero mayor que 1: "))

    
    if numero >=1:
        contador = 0
        limite = round(numero ** 0.5)
        for i in range(1, limite + 1):
            if numero % i == 0:
                contador = contador + 1
        if contador == 1:
            print(f"{numero} es primo.")
        else:
            print(f"{numero} no es primo.")


if __name__ == "__main__":
    main()