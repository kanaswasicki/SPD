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
    Cmax = 0
    while (NN != [] or NG != []):
        while (NN != [] and t >= min(NN)[0]):
            j = NN.index(min(NN))
            NG.append(NN[j])
            NN.pop(j)

        if NG == []:
            t = min(NN)[0]
        else:
            i = NG.index(max(NG, key=operator.itemgetter(2)))
            j = NG[i]
            NG.pop(i)
            teta.append(j)
            t = t + j[1]
            Cmax = max(Cmax, t+j[2])
    return teta, Cmax


def schragepmtn(N):
    teta = []
    NG = []
    NN = copy.deepcopy(N)
    t = min(NN)[0]
    Cmax = 0
    l = [0, 0, 100000000]
    while (NN != [] or NG != []):
        while (NN != [] and t >= min(NN)[0]):
            i = NN.index(min(NN))
            j = NN[i]
            NG.append(j)
            NN.pop(i)
            if j[2] > l[2]:
                l[1] = t - j[0]
                t = j[0]
                if l[1] > 0:
                    NG.append(l)
        if NG == []:
            t = min(NN)[0]
        else:
            i = NG.index(max(NG, key=operator.itemgetter(2)))
            j = NG[i]
            NG.pop(i)
            teta.append(j)
            l = j
            t = t + j[1]
            Cmax = max(Cmax, t+j[2])
    return teta, Cmax


a = []
instancje = [50, 100, 200]
for i in instancje:
    plik = "SPD4\\in" + str(i)+".txt"
    tabela = przygotowanie_danych(plik)
    kolejnosc, Cmax = schragepmtn(tabela)
    a.append(Cmax)
    print(Cmax)
print(sum(a))
