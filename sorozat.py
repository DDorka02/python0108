import random


def listaba():
    dobas = []
    for i in range(7):
        dobasok = random.randrange(0, 2)
        dobas.append(dobasok)
    return dobas


def kiir(lista):
    print("II/A, B, C:", end="\n\t")
    for i in range(len(lista)-1):
        if lista[i] == 0:
            print("FEJ", end="-")
        else:
            print("ÍRÁS", end="-")
    if lista[-1] == 0:
        print("FEJ")
    else:
        print("ÍRÁS")


def fejek_szama(lista):
    db = 0
    for i in range(len(lista)):
        if lista[i]:
            db += 1
    return db


def konzol_kiir(db: int):
    print(f"II/D, E:\n\tA fejek száma: {db}")


def file_kiir(db: int):
    f = open("fejek.txt", "w", encoding="Utf8")
    f.write(f"II/F:\n\tA fejek száma: {db}")
    f.close()
