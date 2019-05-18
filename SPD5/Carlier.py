import operator
import copy
from prettytable import PrettyTable


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
    #


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


def Carlier(n, tabela, wejscie, poziom):
    global best_pi
    global UB
    pi, U = schrage(tabela)
    #print(wejscie, poziom, "\n")
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
    LBL = schragepmtn(tabela)
    tabela[c][0] = max(tabela[c][0], rK+pK)
    temp = tabela[c]
    #LBL = schragepmtn(tabela)
    hkc = min(rK, tabela[c][0])+pK+tabela[c][1]+min(qK, tabela[c][2])
    LBL1 = max(hK, LBL, hkc)
    if LBL1 < UB:
        Carlier(best_pi, tabela, 'lewo', poziom+1)
    tabela[c][0] = tempR

    # PRAWA

    tempQ = tabela[c][2]
    LBP = schragepmtn(tabela)
    tabela[c][2] = max(tabela[c][2], qK + pK)
    temp1 = tabela[c]
    hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
    #LBP = schragepmtn(tabela)
    LBP1 = max(hK, hkc, LBP)
    if LBP1 < UB:
        Carlier(best_pi, tabela, 'prawo', poziom+1)
    tabela[c][2] = tempQ


x = PrettyTable()
x.field_names = ["Carlier", "Permutacja", "Cmax"]
for i in range(0, 9):
    plik = 'data'+str(i)+'.txt'
    tabela, n = przygotowanie_danych(plik)
    UB = 99999999
    Carlier(n, tabela, 'srodek', 0)
    print(UB, '\n')
    best_pi = [x+1 for x in best_pi]
    print(best_pi, '\n')
    x.add_row([plik, best_pi, UB])
print(x)
