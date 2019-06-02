import copy
import Schrage
from prettytable import PrettyTable
import Carlier_dodatkowe as Cd
import time

# wszystko teraz pracuje na zmiennych globalnych, zmieniłem sposob liczenia K
# wyswietla sie tez poziom i kierunek


def Carlier3(tabela):
    global best_pi
    global UB
    global cofniecie
    pi, U = Schrage.schrage(tabela)
    if U < UB:
        UB = U
        best_pi = pi
    b = Cd.licz_b(U, pi, tabela)
    a = Cd.licz_a(U, pi, tabela, b)
    c = Cd.licz_c(pi, tabela, a, b)
    if c == []:
        cofniecie += 1
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
        Carlier3(tabela)
    tabela[c][2] = tempQ
    if cofniecie == 1:
        tempR = tabela[c][0]
        LB = Schrage.schragepmtn(tabela)
        tabela[c][0] = max(tabela[c][0], rK + pK)
        hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
        LBL = max(hK, LB, hkc)
        if LBL < UB:
            cofniecie = 0
            Carlier3(tabela)
        tabela[c][0] = tempR


def Carlier2(tabela):
    global best_pi
    global UB
    global cofniecie
    pi, U = Schrage.schrage(tabela)
    if U < UB:
        UB = U
        best_pi = pi
    b = Cd.licz_b(U, pi, tabela)
    a = Cd.licz_a(U, pi, tabela, b)
    c = Cd.licz_c(pi, tabela, a, b)
    if c == []:
        cofniecie += 1
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
        cofniecie = 0
        Carlier2(tabela)
    tabela[c][0] = tempR
    if cofniecie == 1:
        tempQ = tabela[c][2]
        LB = Schrage.schragepmtn(tabela)
        tabela[c][2] = max(tabela[c][2], qK + pK)
        hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
        LBP = max(hK, hkc, LB)
        if LBP < UB:
            Carlier2(tabela)
        tabela[c][2] = tempQ


def Carlierdeepleft(tabela):
    global best_pi
    global UB
    global n
    pi, U = Schrage.schrage(tabela)
    #print(wejscie, poziom, "\n")
    if U < UB:
        UB = U
        best_pi = pi
    b = Cd.licz_b(U, pi, tabela)
    a = Cd.licz_a(U, pi, tabela, b)
    c = Cd.licz_c(pi, tabela, a, b)
    if c == []:
        return
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
    rpq = [rK, pK, qK]
    LB = Schrage.schragepmtn(tabela)
    # LEWA
    tempR = tabela[c][0]
    tabela[c][0] = max(tabela[c][0], rK+pK)
    hkc = min(rK, tabela[c][0])+pK+tabela[c][1]+min(qK, tabela[c][2])
    LBL = max(sum(rpq), LB, hkc)
    if LBL < UB:
        Carlierdeepleft(tabela)
    tabela[c][0] = tempR
    # PRAWA
    tempQ = tabela[c][2]
    tabela[c][2] = max(tabela[c][2], qK + pK)
    hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
    LBP = max(sum(rpq), hkc, LB)
    if LBP < UB:
        Carlierdeepleft(tabela)
    tabela[c][2] = tempQ


def Carlierdeeplefteliminacja(tabela):
    global best_pi
    global UB
    global n

    pi, U = Schrage.schrage(tabela)
    if U < UB:
        UB = U
        best_pi = pi
    b = Cd.licz_b(U, pi, tabela)
    a = Cd.licz_a(U, pi, tabela, b)
    c = Cd.licz_c(pi, tabela, a, b)
    if c == []:
        return
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
    rpq = [rK, pK, qK]
    L = Cd.wyznacz_L(pi, c, b, UB, rpq, tabela)
    LB = Schrage.schragepmtn(tabela)
    tabela = Cd.eliminacja(L, tabela, UB, rpq, b)
    # LEWA
    tempR = tabela[c][0]
    tabela[c][0] = max(tabela[c][0], rK+pK)
    hkc = min(rK, tabela[c][0])+pK+tabela[c][1]+min(qK, tabela[c][2])
    LBL = max(sum(rpq), LB, hkc)
    if LBL < UB:
        Carlierdeeplefteliminacja(tabela)
    tabela[c][0] = tempR
    # PRAWA
    tempQ = tabela[c][2]
    tabela[c][2] = max(tabela[c][2], qK + pK)
    hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
    #LBP = schragepmtn(tabela)
    LBP = max(sum(rpq), hkc, LB)
    if LBP < UB:
        Carlierdeeplefteliminacja(tabela)
    tabela[c][2] = tempQ


def Carlierwidelefteliminacja():
    global tab_task
    global best_pi
    global UB
    global n
    if tab_task == []:
        return
    tabela = tab_task[0]
    tab_task.pop(0)
    pi, U = Schrage.schrage(tabela)
    if U < UB:
        UB = U
        best_pi = pi
    b = Cd.licz_b(U, pi, tabela)
    a = Cd.licz_a(U, pi, tabela, b)
    c = Cd.licz_c(pi, tabela, a, b)
    if c == []:
        return
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
    rpq = [rK, pK, qK]
    L = Cd.wyznacz_L(pi, c, b, UB, rpq, tabela)
    LB = Schrage.schragepmtn(tabela)
    tabela = Cd.eliminacja(L, tabela, UB, rpq, b)
    # LEWA
    tempR = tabela[c][0]
    tabela[c][0] = max(tabela[c][0], rK+pK)
    hkc = min(rK, tabela[c][0])+pK+tabela[c][1]+min(qK, tabela[c][2])
    LBL = max(sum(rpq), LB, hkc)
    if LBL < UB:
        tab_task.append(copy.deepcopy(tabela))
    tabela[c][0] = tempR
    # PRAWA
    tempQ = tabela[c][2]
    tabela[c][2] = max(tabela[c][2], qK + pK)
    hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
    LBP = max(sum(rpq), hkc, LB)
    if LBP < UB:
        tab_task.append(copy.deepcopy(tabela))
    tabela[c][2] = tempQ
    Carlierwidelefteliminacja()

def Carlierwideleft():
    global tab_task
    global best_pi
    global UB
    global n
    if tab_task == []:
        return
    tabela = tab_task[0]
    tab_task.pop(0)
    pi, U = Schrage.schrage(tabela)
    if U < UB:
        UB = U
        best_pi = pi
    b = Cd.licz_b(U, pi, tabela)
    a = Cd.licz_a(U, pi, tabela, b)
    c = Cd.licz_c(pi, tabela, a, b)
    if c == []:
        return
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
    rpq = [rK, pK, qK]
    LB = Schrage.schragepmtn(tabela)
    # LEWA
    tempR = tabela[c][0]
    tabela[c][0] = max(tabela[c][0], rK+pK)
    hkc = min(rK, tabela[c][0])+pK+tabela[c][1]+min(qK, tabela[c][2])
    LBL = max(sum(rpq), LB, hkc)
    if LBL < UB:
        tab_task.append(copy.deepcopy(tabela))
    tabela[c][0] = tempR
    # PRAWA
    tempQ = tabela[c][2]
    tabela[c][2] = max(tabela[c][2], qK + pK)
    hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
    LBP = max(sum(rpq), hkc, LB)
    if LBP < UB:
        tab_task.append(copy.deepcopy(tabela))
    tabela[c][2] = tempQ
    Carlierwideleft()


x = PrettyTable()
#x.field_names = ["wykonane zadanie", "Deep left", "Deep left z eliminacja", "Wide left", "Wide left z eliminacja", "Autorska 1", "Autorska 2"]
x.field_names = ["Deep left","uszeregowanie", "UB"]
tab_task = []
for i in range(5,6):
    plik = 'data'+str(i)+'.txt'
    tabela, n = Schrage.przygotowanie_danych(plik)
    UB = 99999999
    cofniecie = 0
    tab_task.append(tabela)
    duration = time.time()
    Carlierdeepleft(tabela)
    duration = time.time() - duration
    print(UB, '\n')
    #best_pi = [x+1 for x in best_pi]
    #print(best_pi, '\n')
    x.add_row([plik, best_pi,UB])
print(x)
