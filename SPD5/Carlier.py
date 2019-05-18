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
            teta.append(N.index(j))
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
    return Cmax


def licz_b(U, n, tabela):
    p = 0
    for i in n:
        r = tabela[i][0]
        p = max(p, r) + tabela[i][1]
        if U == p + tabela[i][2]:
            j = i
    return j


def licz_a(U, n, tabela, b):
    q = tabela[b][2]
    mx = n.index(b)
    for i in n:
        p = 0
        r = tabela[i][0]
        mi = n.index(i)
        for a in range(mi, mx+1):
            p += tabela[n[a]][1]
        if U == r+p+q:
            return i


def licz_c(n, tabela, a, b):
    flaga = 0
    a = n.index(a)
    b = n.index(b)
    for i in range(a, b+1):
        if tabela[n[i]][2] < tabela[n[b]][2]:
            j = n[i]
            flaga = 1
    if flaga == 1:
        return j
    else:
        return []

# wszystko teraz pracuje na zmiennych globalnych, zmieniłem sposob liczenia K
# wyswietla sie tez poziom i kierunek
def Carlier(n, tabela,wejscie, poziom):
    global best_pi
    global UB
    pi, U = schrage(tabela)
    print(wejscie, poziom, "\n")
    if U < UB:
        UB = U
        best_pi = pi
    b = licz_b(U, pi, tabela)
    a = licz_a(U, pi, tabela, b)
    c = licz_c(pi, tabela, a, b)
    if c == []:
        return UB, tabela
    K = []
    for i in pi[pi.index(c)+1:pi.index(b)+1]:
        K.append(i)
    rK = []
    qK = []
    pK = 0
    for i in K:
        rK.append(tabela[i][0])
        qK.append(tabela[i][2])
        pK += tabela[i][1]
    qK = min(qK)
    rK = min(rK)
    hK = rK+pK+qK
    # LEWA

    tempR = tabela[c][0]
    tabela[c][0] = max(tabela[c][0], rK+pK)
    temp = tabela[c]
    LB = schragepmtn(tabela)
    hkc = min(rK, tabela[c][0])+pK+tabela[c][1]+min(qK, tabela[c][2])
    LB = max(hK, LB, hkc)
    if LB < UB:
        Carlier(best_pi, tabela, 'lewo',poziom+1)
    tabela[c][0] = tempR

    # PRAWA

    tempQ = tabela[c][2]
    tabela[c][2] = max(tabela[c][2], qK + pK)
    temp1 = tabela[c]
    hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
    LB = schragepmtn(tabela)
    LB = max(hK, hkc, LB)
    if LB < UB:
        Carlier(best_pi, tabela, 'prawo', poziom+1)
    tabela[c][2] = tempQ



plik = "data3.txt"
tabela, n = przygotowanie_danych(plik)
UB = 99999999
Carlier(n, tabela, 'srodek', 0)
print(UB, tabela)
best_pi = [x+1 for x in best_pi]
print(best_pi)
