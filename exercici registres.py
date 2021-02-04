#Implementa una aplicació que demani (i validi) les següents dades per teclat (registre):
#-aula: numèric (entre 1 i 50)
#-nom aula: text
#-ip: text
#-nombre pcs: numèric (entre 1 i 20)
#Demana quants registres vol introduir i mostrar els resultats en forma de taula.

def main():
    thisdict = {}

    x = int(input("Introdueix el nombre de registres que vols fer: "))
    fnumaula = []
    fnomaula = []
    fip = []
    fnumpcs = []
    for i in range(x):
        numaula = int(input("Quin és el número d'aula? "))
        fnumaula.append(numaula)
        thisdict["Número d'aula"] = fnumaula
        nomaula = input("Quin és el nom de l'aula? ")
        fnomaula.append(nomaula)
        thisdict["Nom d'aula"] = fnomaula
        ip = (input ("Quina és la IP? "))
        fip.append(ip)
        thisdict["IP"] = fip
        numpcs = int(input("Quin és el número de PCs? "))
        fnumpcs.append(numpcs)
        thisdict["Número de PCs"] = fnumpcs

    print(thisdict)


if __name__ == "__main__":
    main()