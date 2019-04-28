import operator
import copy


def odczyt(nazwa):
    theFile = open(nazwa, "r")
    theFloats = []
    for val in theFile.read().split():
        theFloats.append(float(val))
    theFile.close()
    return theFloats


# segregowanie danych do pozniejszego wykorzystania w algorytmie


def przygotowanie_danych(nazwa):
    Wartosci = odczyt(nazwa)
    tabela = []
    for a in range(2, len(Wartosci), 3):
        tabela_pomocnicza = []
        for b in range(0, 3):
            tabela_pomocnicza = tabela_pomocnicza + [Wartosci[a + b]]
        tabela.append(tabela_pomocnicza)
    return tabela


def schrage(N):
    teta = []
    NG = []
    NN = copy.deepcopy(N)
    t = min(NN)[0]
    while (NN != [] or NG != []):
        while (NN != [] and t >= min(NN)[0]):
            j = [NN.index(min(NN))]
            j.extend(NN[j[0]])
            NG.append(j)
            NN.pop(j[0])

        if NG == []:
            t = min(NN)[0]
        else:
            j = NG.index(max(NG, key=operator.itemgetter(3)))

            teta.append(NG[j][0])
            t = t + NG[j][2]
            NG.pop(j)
    return teta


def licz_Cmax(kolejnosc, tabela):
    r = 0
    p = 0
    Cmax = 0
    for a in kolejnosc:
        r += tabela[a][0]
        p = max(p, r) + tabela[a][1]
        Cmax = max(Cmax, p+tabela[a][2])
    return Cmax


plik = "SPD4\\in200.txt"
tabela = przygotowanie_danych(plik)
kolejnosc = schrage(tabela)
print(kolejnosc)
Cmax = licz_Cmax(kolejnosc, tabela)
print(Cmax)
