

def main():
    aprovats = []
    suspesos = []

    not1 = int(input("Afegeix la 1a nota "))
    suspesos.extend([not1]) if not1 < 5 else aprovats.extend([not1])
    not2 = int(input("Afegeix la 2a nota "))
    suspesos.extend([not2]) if not2 < 5 else aprovats.extend([not2])
    not3 = int(input("Afegeix la 3a nota "))
    suspesos.extend([not3]) if not3 < 5 else aprovats.extend([not3])
    not4 = int(input("Afegeix la 4a nota "))
    suspesos.extend([not4]) if not4 < 5 else aprovats.extend([not4])
    not5 = int(input("Afegeix la 5a nota "))
    suspesos.extend([not5]) if not5 < 5 else aprovats.extend([not5])
    not6 = int(input("Afegeix la 6a nota "))
    suspesos.extend([not6]) if not6 < 5 else aprovats.extend([not6])
    not7 = int(input("Afegeix la 7a nota "))
    suspesos.extend([not7]) if not7 < 5 else aprovats.extend([not7])
    not8 = int(input("Afegeix la 8a nota "))
    suspesos.extend([not8]) if not8 < 5 else aprovats.extend([not8])
    not9 = int(input("Afegeix la 9a nota "))
    suspesos.extend([not9]) if not9 < 5 else aprovats.extend([not9])
    not10 = int(input("Afegeix la 10a nota "))
    suspesos.extend([not10]) if not10 < 5 else aprovats.extend([not10])
    not11 = int(input("Afegeix la 11a nota "))
    suspesos.extend([not11]) if not11 < 5 else aprovats.extend([not11])
    not12 = int(input("Afegeix la 12a nota "))
    suspesos.extend([not12]) if not12 < 5 else aprovats.extend([not12])
    not13 = int(input("Afegeix la 13a nota "))
    suspesos.extend([not13]) if not13 < 5 else aprovats.extend([not13])
    not14 = int(input("Afegeix la 14a nota "))
    suspesos.extend([not14]) if not14 < 5 else aprovats.extend([not14])
    not15 = int(input("Afegeix la 15a nota "))
    suspesos.extend([not15]) if not15 < 5 else aprovats.extend([not15])

    #a = mitjana_aprovats
    #b = mitjana_suspesos

    a = sum(aprovats) / len(aprovats)
    print("La mitjana d'aprovats és: ",a)

    b = sum(suspesos) / len(suspesos)
    print("La mitjana de suspesos és: ",b)

    x=len(aprovats)
    y=len(suspesos)

    print("El nombre d'aprovats és: ", x)
    print("El nombre de suspesos és: ", y)


if __name__ == "__main__":
    main()
