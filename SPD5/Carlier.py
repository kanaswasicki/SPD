
import copy
import Schrage
from prettytable import PrettyTable
import Carlier_dodatkowe as Cd


# wszystko teraz pracuje na zmiennych globalnych, zmieniłem sposob liczenia K
# wyswietla sie tez poziom i kierunek
def Carlier3(n, tabela, wejscie, poziom):
    global best_pi
    global UB
    global cofniecie
    pi, U = Schrage.schrage(tabela)
    print(wejscie, poziom, "\n")
    if U < UB:
        UB = U
        best_pi = pi
    b = Cd.licz_b(U, pi, tabela)
    a = Cd.licz_a(U, pi, tabela, b)
    c = Cd.licz_c(pi, tabela, a, b)
    if c == []:
        cofniecie+=1
        return UB, tabela
    K = []
    for i in pi[pi.index(c) + 1:pi.index(b) + 1]:
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
    hK = rK + pK + qK

    # LEWA
    tempQ = tabela[c][2]
    LB = Schrage.schragepmtn(tabela)
    tabela[c][2] = max(tabela[c][2], qK + pK)
    hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
    LBP = max(hK, hkc, LB)
    if LBP < UB:
        Carlier3(best_pi, tabela, 'prawo', poziom + 1)
    tabela[c][2] = tempQ
    if cofniecie == 1:
        tempR = tabela[c][0]
        LB = Schrage.schragepmtn(tabela)
        tabela[c][0] = max(tabela[c][0], rK + pK)
        hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
        LBL = max(hK, LB, hkc)
        if LBL < UB:
            cofniecie = 0
            Carlier3(best_pi, tabela, 'lewo', poziom + 1)
        tabela[c][0] = tempR

def Carlier2(n, tabela, wejscie, poziom):
    global best_pi
    global UB
    global cofniecie
    pi, U = Schrage.schrage(tabela)
    print(wejscie, poziom, "\n")
    if U < UB:
        UB = U
        best_pi = pi
    b = Cd.licz_b(U, pi, tabela)
    a = Cd.licz_a(U, pi, tabela, b)
    c = Cd.licz_c(pi, tabela, a, b)
    if c == []:
        cofniecie+=1
        return UB, tabela
    K = []
    for i in pi[pi.index(c) + 1:pi.index(b) + 1]:
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
    hK = rK + pK + qK

    # LEWA

    tempR = tabela[c][0]
    LB = Schrage.schragepmtn(tabela)
    tabela[c][0] = max(tabela[c][0], rK + pK)
    hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
    LBL = max(hK, LB, hkc)
    if LBL < UB:
        cofniecie=0
        Carlier2(best_pi, tabela, 'lewo', poziom + 1)
    tabela[c][0] = tempR
    if cofniecie == 1:
        tempQ = tabela[c][2]
        LB = Schrage.schragepmtn(tabela)
        tabela[c][2] = max(tabela[c][2], qK + pK)
        hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
        LBP = max(hK, hkc, LB)
        if LBP < UB:
            Carlier2(best_pi, tabela, 'prawo', poziom + 1)
        tabela[c][2] = tempQ


def Carlier(n, tabela, wejscie, poziom):
    global best_pi
    global UB
    pi, U = Schrage.schrage(tabela)
    #print(wejscie, poziom, "\n")
    if U < UB:
        UB = U
        best_pi = pi
    b = Cd.licz_b(U, pi, tabela)
    a = Cd.licz_a(U, pi, tabela, b)
    c = Cd.licz_c(pi, tabela, a, b)
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
    LB = Schrage.schragepmtn(tabela)
    tabela[c][0] = max(tabela[c][0], rK+pK)
    temp = tabela[c]
    hkc = min(rK, tabela[c][0])+pK+tabela[c][1]+min(qK, tabela[c][2])
    LBL = max(hK, LB, hkc)
    if LBL < UB:
        Carlier(best_pi, tabela, 'lewo', poziom+1)
    tabela[c][0] = tempR

    # PRAWA

    tempQ = tabela[c][2]
    LB = Schrage.schragepmtn(tabela)
    tabela[c][2] = max(tabela[c][2], qK + pK)
    temp1 = tabela[c]
    hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
    #LBP = schragepmtn(tabela)
    LBP = max(hK, hkc, LB)
    if LBP < UB:
        Carlier(best_pi, tabela, 'prawo', poziom+1)
    tabela[c][2] = tempQ



x = PrettyTable()
x.field_names = ["Carlier", "Permutacja", "Cmax"]
for i in range(0, 9):
    plik = 'data'+str(i)+'.txt'
    tabela, n =Schrage.przygotowanie_danych(plik)
    UB = 99999999
    cofniecie = 0
    Carlier2(n, tabela, 'srodek', 0)
    print(UB, '\n')
    #best_pi = [x+1 for x in best_pi]
    print(best_pi, '\n')
    x.add_row([plik, best_pi, UB])
print(x)
