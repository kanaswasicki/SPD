import operator
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
    n = int(Wartosci[0])
    for a in range(2, len(Wartosci), 3):
        tabela_pomocnicza = []
        for b in range(0, 3):
            tabela_pomocnicza = tabela_pomocnicza + [Wartosci[a + b]]
        tabela.append(tabela_pomocnicza)
    return tabela, n


def schrage(N):
    teta = []
    NG = []
    NN = []
    a = 0
    for i in N:
        NN.append([a, i[0], i[1], i[2]])
        a += 1
    t = min(NN, key=operator.itemgetter(1))[1]
    Cmax = 0
    while (NN != [] or NG != []):
        while (NN != [] and t >= min(NN, key=operator.itemgetter(1))[1]):
            j = NN.index(min(NN, key=operator.itemgetter(1)))
            NG.append(NN[j])
            NN.pop(j)

        if NG == []:
            t = min(NN, key=operator.itemgetter(1))[1]
        else:
            i = NG.index(max(NG, key=operator.itemgetter(3)))
            j = NG[i]
            NG.pop(i)
            teta.append(j[0])
            t = t + j[2]
            Cmax = max(Cmax, t+j[3])
    return teta, Cmax


def schragepmtn(N):
    NG = []
    NN = []
    a = 0
    for i in N:
        NN.append([a, i[0], i[1], i[2]])
        a += 1
    t = min(NN, key=operator.itemgetter(1))[1]
    Cmax = 0
    l = [0, 0, 0, 100000000]
    while (NN != [] or NG != []):
        while (NN != [] and t >= min(NN, key=operator.itemgetter(1))[1]):
            j = NN.index(min(NN, key=operator.itemgetter(1)))
            i = NN[j]
            NG.append(NN[j])
            NN.pop(j)
            if i[3] > l[3]:
                l[2] = t - i[1]
                t = i[1]
                if l[2] > 0:
                    NG.append(l)
        if NG == []:
            t = min(NN, key=operator.itemgetter(1))[1]
        else:
            i = NG.index(max(NG, key=operator.itemgetter(3)))
            j = NG[i]
            NG.pop(i)
            l = j
            t = t + j[2]
            Cmax = max(Cmax, t+j[3])
    return Cmax