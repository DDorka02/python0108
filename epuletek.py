import Epulet


def listaba():
    epuletek = []
    f = open("epulet.txt", "r", encoding="utf8")
    f.readline()
    sorok = f.readlines()
    f.close()
    # print(sorok)
    for i in range(len(sorok)):
        epulet = Epulet.Epulet(sorok[i])
        epuletek.append(epulet)
    return epuletek


def kiiratas(lista: list[Epulet.Epulet]):
    print(f"III/A, B:\n\t Az épületek száma: {len(lista)}")


def nagyobb(lista):
    db = 0
    lab = 3.280839895
    for i in range(len(lista)):
        if lista[i].magassag * lab > 555:
            db += 1
    return f"III/C: \n\t 555 lábnál magasabb épületek száma: {db}"


def legoregebb(lista: list[Epulet.Epulet]):
    lego = 0
    for i in range(1, len(lista)):
        if lista[lego].ev > lista[i].ev:
            lego = i
    return f"III/D: \n\t Legöregegebb épület országa: {lista[lego].orszag}"
