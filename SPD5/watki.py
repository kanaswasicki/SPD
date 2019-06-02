from __future__ import with_statement

import copy
import threading
import time

from prettytable import PrettyTable

import Carlier_dodatkowe as Cd
import Schrage

global best_pi
global UB
global n
UB_lock = threading.Lock()


def CarlierEliminacja(tabela):
    global best_pi
    global UB
    global n
    flaga1 = 0
    flaga2 = 0
    pi, U = Schrage.schrage(tabela)
    UB_lock.acquire()
    if U < UB:
        UB = U
        best_pi = pi
    UB_lock.release()
    b = Cd.licz_b(U, pi, tabela)
    a = Cd.licz_a(U, pi, tabela, b)
    c = Cd.licz_c(pi, tabela, a, b)
    if c == []:
        return
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
    rpq = [rK, pK, qK]
    L = Cd.wyznacz_L(pi, c, b, UB, rpq, tabela)
    LB = Schrage.schragepmtn(tabela)
    tabela = Cd.eliminacja(L, tabela, UB, rpq, b)
    # LEWA
    tempR = tabela[c][0]
    tabela[c][0] = max(tabela[c][0], rK + pK)
    hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
    LBL = max(sum(rpq), LB, hkc)
    UB_lock.acquire()
    if LBL < UB:
        w1 = Carlier_Eliminacja(copy.deepcopy(tabela))
        flaga1 = 1
    UB_lock.release()
    tabela[c][0] = tempR
    # PRAWA
    tempQ = tabela[c][2]
    tabela[c][2] = max(tabela[c][2], qK + pK)
    hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
    # LBP = schragepmtn(tabela)
    LBP = max(sum(rpq), hkc, LB)
    UB_lock.acquire()
    if LBP < UB:
        w2 = Carlier_Eliminacja(copy.deepcopy(tabela))

        flaga2 = 1
    UB_lock.release()
    tabela[c][2] = tempQ

    tabela[c][2] = tempQ
    if flaga1 == 1:
        w1.start()
    if flaga2 == 1:
        w2.start()
    if flaga1 == 1:
        w1.join()
    if flaga2 == 1:
        w2.join()


def Carlier(tabela):
    global best_pi
    global UB
    global n
    flaga1 = 0
    flaga2 = 0
    pi, U = Schrage.schrage(tabela)
    UB_lock.acquire()
    if U < UB:
        UB = U
        best_pi = pi
    UB_lock.release()
    b = Cd.licz_b(U, pi, tabela)
    a = Cd.licz_a(U, pi, tabela, b)
    c = Cd.licz_c(pi, tabela, a, b)
    if c == []:
        return
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
    UB_lock.acquire()
    if LBL < UB:
        w1 = Carlier_podstawowy(copy.deepcopy(tabela))
        flaga1 = 1
    UB_lock.release()
    tabela[c][0] = tempR

    # PRAWA
    tempQ = tabela[c][2]
    LB = Schrage.schragepmtn(tabela)
    tabela[c][2] = max(tabela[c][2], qK + pK)
    hkc = min(rK, tabela[c][0]) + pK + tabela[c][1] + min(qK, tabela[c][2])
    LBP = max(hK, hkc, LB)
    UB_lock.acquire()
    if LBP < UB:
        w2 = Carlier_podstawowy(copy.deepcopy(tabela))
        flaga2 = 1
    UB_lock.release()
    tabela[c][2] = tempQ
    if flaga1 == 1:
        w1.start()
        w1.join()
    if flaga2 == 1:
        w2.start()
    if flaga1 == 1:
        w1.join()
    if flaga2 == 1:
        w2.join()


class Carlier_Eliminacja(threading.Thread):
    def __init__(self, value):
        threading.Thread.__init__(self)
        self.value = value

    def run(self):
        CarlierEliminacja(self.value)


# kazde zadanie obliczeniowe uruchamiane jest w osobnym watku
class Carlier_podstawowy(threading.Thread):

    def __init__(self, value):
        threading.Thread.__init__(self)
        self.value = value

    def run(self):
        Carlier(self.value)


x = PrettyTable()
x.field_names = ["Carlier", "Permutacja", "Cmax", "czas wykonania"]
for i in range(3, 4):
    plik = 'data' + str(i) + '.txt'
    tabela, n = Schrage.przygotowanie_danych(plik)
    UB = 99999999

    w = Carlier_Eliminacja(copy.deepcopy(tabela))
    duration = time.time()
    w.start()
    while (1):
        print(threading.activeCount())
    w.join()
    time.sleep(5)
    duration = time.time() - duration
    print(UB, '\n')
    # best_pi = [x+1 for x in best_pi]
    print(best_pi, '\n')
    x.add_row([plik, best_pi, UB, duration])
print(x)
