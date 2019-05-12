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


def licz_b(U, n, tabela):
    for i in range(0, n):
        r = tabela[i][0]
        p = max(p, r) + tabela[i][1]
        Cmax = max(Cmax, p + tabela[i][2])
        if U = Cmax:
            j = i
    return j


def licz_a(U, n, tabela, b):
    q = tabela[b][2]
    for i in range(0, n):
        p = 0
        for a in range(i, b):
            p += tabela[a][1]
        if U = tabela[i][0]+p+q:
            return i


def licz_c(tabela, a, b):
    for i in range(a, b):
        if tabela[i][2] < tabela[b][2]:
            j = i
            flaga = 1
    if flaga == 1:
        return j
    else:
        return []


def Carlier(n, tabela):
    UB = 99999999999
    pi, U = schrage(tabela)
    if U < UB:
        UB = U
        tabela = pi
    b = licz_b(U, n, tabela)
    a = licz_a(U, n, tabela, b)
    c = licz_c(tabela, a, b)
    if c == []:
        return tabela, UB
    K = []
    for i in range(c+1, b+1):
        K.append(i)
    rK = []
    qK = []
    pK = 0
    for i in K:
        rK.append(tabela[i][0])
        qK.append(tabela[i][2])
        pK += tabela[i][1]
    qK = max(qK)
    rK = min(rK)
    hK = rK+pK+qK
    hkc = min(rk, tabela[c][0])+pK+tabela[c][1]+max(qK, tabela[c][2])
    rc = max(tabela[c][0], rK+pK)
    LB = schragepmtn(tabela)
    LB = max(hK, LB, hkc)
    if LB < UB:
        Carlier(n, tabela)
    rc = tabela[c][0]
    qc = max(tabela[c][2], qK+pK)
    LB = schragepmtn(tabela)
    LB = max(hK, hkc, LB)
    if LB < UB:
        Carlier(n, tabela)
    qc = tabela[c][2]
