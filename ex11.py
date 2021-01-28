

def main():
    aprovats = []
    suspesos = []

    for i in range(15):
        nota = int(input("Introdueix una nota; "))
        if nota < 5:
            suspesos.append(nota)
        else:
            aprovats.append(nota)

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
