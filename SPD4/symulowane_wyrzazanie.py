import copy
import random

import math


def odczyt(nazwa):
    theFile = open(nazwa, "r")
    theFloats = []
    for val in theFile.read().split():
        theFloats.append(float(val))
    theFile.close()
    return theFloats


def obliczenie_Cmax(kolejnosc, tabela):
    p = 0
    Cmax = 0
    for a in kolejnosc:
        r = tabela[a][0]
        p = max(p, r) + tabela[a][1]
        Cmax = max(Cmax, p + tabela[a][2])
    return Cmax


def przygotowanie_danych(nazwa):
    Wartosci = odczyt(nazwa)
    tabela = []
    n = int(Wartosci[0])
    ilosc = int(Wartosci[1])
    for a in range(2, len(Wartosci), ilosc):
        tabela_pomocnicza = []
        for b in range(0, ilosc):
            tabela_pomocnicza = tabela_pomocnicza + [Wartosci[a + b]]
        tabela.append(tabela_pomocnicza)
    return tabela, n, ilosc


"""

Od tego miejsca zaczynają sie przydatne funkcje

"""


# inicjalizacja 1. rozwiazania ale tez ustawienie parametrów


def inicjalizacja(ilosc_zadan, temperatura, Wspolczynnik_schladzania):
    lista = list(range(0, ilosc_zadan))
    random.shuffle(lista)
    return lista, temperatura, Wspolczynnik_schladzania


# tworzenie ruchu typu swap
def generowanie_ruchu_swap(rozwiazanie):
    pozycje = random.sample(range(len(rozwiazanie)), k=2)
    para = rozwiazanie[pozycje[0]], rozwiazanie[pozycje[1]]
    rozwiazanie_swap = copy.deepcopy(rozwiazanie)
    rozwiazanie_swap[pozycje[1]], rozwiazanie_swap[pozycje[0]] = para
    return rozwiazanie_swap


# tworzenie ruchu typu insert


def generowanie_ruchu_insert(rozwiazanie):
    pozycja_do_przestawienia = random.sample(range(len(rozwiazanie)), k=1)
    wylosowane_zadanie = rozwiazanie[pozycja_do_przestawienia[0]]
    wylosowana_pozycja = random.sample(range(len(rozwiazanie)), k=2)
    rozwiazanie_insert = copy.deepcopy(rozwiazanie)
    if wylosowana_pozycja[0] == pozycja_do_przestawienia[0]:
        rozwiazanie_insert.pop(pozycja_do_przestawienia[0])
        rozwiazanie_insert.insert(wylosowana_pozycja[1], wylosowane_zadanie)
    else:
        rozwiazanie_insert.pop(pozycja_do_przestawienia[0])
        rozwiazanie_insert.insert(wylosowana_pozycja[0], wylosowane_zadanie)
    return rozwiazanie_insert


# podstawowa funkcja decyzyjna, dajjemy p=1 dla lepszych rozwiazan
def decyzja(cmax_przed, cmax_po, rozwiazanie_po, rozwiazanie_przed):
    if cmax_po < cmax_przed:
        return rozwiazanie_po, cmax_po
    else:  # rozpisane tak dokładnie aby istniala mozliwosc sledzenia wartosci prawdopodobienstwa w debuggerze
        p = math.exp((cmax_przed - cmax_po) / Temperatura)
        prand = random.random()
        if p >= prand:
            return rozwiazanie_po, cmax_po
        else:
            return rozwiazanie_przed, cmax_przed


# alternatywna funkcja decyzyjna, nie dajemy 1 dla lepszych rozwiazan
def decyzja_mod(cmax_przed, cmax_po, rozwiazanie_po, rozwiazanie_przed):
    p = math.exp((cmax_przed - cmax_po) / Temperatura)
    prand = random.random()
    if p >= prand:
        return rozwiazanie_po, cmax_po
    else:
        return rozwiazanie_przed, cmax_przed


# podstawowa funkcja schladzania
def schladzanie(temp):
    temp = Wspolczynnik_schladzania * temp
    return temp


# aletrnatywna funkcja schladzania
def schladzanie2(temp, k, kmax):
    temp = temp * k / kmax
    return temp


Temperatura = 5
Wspolczynnik_schladzania = 0.95
