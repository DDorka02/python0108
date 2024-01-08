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
