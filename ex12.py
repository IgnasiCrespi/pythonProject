def main():
    parells = []
    senars = []
    for i in range(10):
        val = int(input("Introdueix un nombre: "))
        if val%2==0:
            parells.append(val)
        else:
            senars.append(val)

    print("Els nombres parells introduïts són: ", parells)
    print("Els nombres senars introduïts són: ", senars)
if __name__ == "__main__":
    main()