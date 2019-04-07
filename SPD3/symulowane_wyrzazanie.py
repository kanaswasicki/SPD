import random
import math
import copy


def odczyt(nazwa):
    theFile = open(nazwa, "r")
    theFloats = []
    for val in theFile.read().split():
        theFloats.append(float(val))
    theFile.close()
    return theFloats


def obliczenie_Cmax(kolejnosc):
    m = [0]*maszyny
    for i in kolejnosc:
        for j in range(0, maszyny):
            if j == 0:
                m[j] += tabela[i][j]
            else:
                m[j] = max(m[j], m[j-1])+tabela[i][j]
    return max(m)


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
        p = math.exp((cmax_przed-cmax_po)/Temperatura)
        prand = random.random()
        if p >= prand:
            return rozwiazanie_po, cmax_po
        else:
            return rozwiazanie_przed, cmax_przed


# alternatywna funkcja decyzyjna, nie dajemy 1 dla lepszych rozwiazan
def decyzja_mod(cmax_przed, cmax_po,  rozwiazanie_po, rozwiazanie_przed):

    p = math.exp((cmax_przed-cmax_po)/Temperatura)
    prand = random.random()
    if p >= prand:
        return rozwiazanie_po, cmax_po
    else:
        return rozwiazanie_przed, cmax_przed


# podstawowa funkcja schladzania
def schladzanie(temp):
    temp = Wspolczynnik_schladzania*temp
    return temp


# aletrnatywna funkcja schladzania
def schladzanie2(temp, k, kmax):

    temp = temp*k/kmax
    return temp


def tabela_latex(tabela_cmax, tabela_sr):
    print('\\begin{tabular}{l|l|c|c}')

    print('Insert & Cmax &Swap & Cmax \\\\ \\hline')
    for i in tabela_cmax:
        print(
            f"--- & {i[0]} & --- & {i[1]}\\\\")
    print('\\hline')
    print(
        f"--- & {tabela_sr[0]} & --- & {tabela_sr[1]}\\\\")
    print('\\hline\\hline')
    print('\\end{tabular}')


# przygotowanie danych
plik = "data.txt"
tabela, n, maszyny = przygotowanie_danych(plik)


# inicjalizacja algorytmu
tabela_cmax = [[0, 0], [0, 0], [0, 0], [0, 0], [
    0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [
    0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [
    0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

for a in range(0, 2):
    if a == 0:
        Rozwiazanie_poczatkowe, Temperatura, Wspolczynnik_schladzania = inicjalizacja(
            n, 20000, 0.80)
    if a == 1:
        Temperatura = 20000
        Wspolczynnik_schladzania = 0.80
        Rozwiazanie_poczatkowe = [2, 8, 13, 16, 6, 10, 1, 14, 4, 11, 9, 19, 0, 12, 5, 18, 15, 3, 17, 7]
    for i in range(0, 30):
        k = 0
        Rozwiazanie_przed = copy.deepcopy(Rozwiazanie_poczatkowe)
        Cmax = obliczenie_Cmax(Rozwiazanie_poczatkowe)
        # głowna petla programu
        Temperatura = 200
        kmax = 500  # maksymalna ilosc iteracji
        TemperaturaMin = 1  # minimalna temperatura
        for k in range(0, kmax):  # kryterium stopu - liczba iteracji
            if Temperatura >= 1:  # kryterium stopu - temperatura graniczna
                Rozwiazanie_po = generowanie_ruchu_swap(Rozwiazanie_przed)
                Cmax_po = obliczenie_Cmax(Rozwiazanie_po)
                # odrucenie rozwiazan z takim samym Cmax (modyfikacja)
                if Cmax_po != Cmax:
                    Rozwiazanie_po_decyzji, Cmax = decyzja(
                        Cmax, Cmax_po, Rozwiazanie_po, Rozwiazanie_przed)
                    Temperatura = schladzanie(Temperatura)
                    Rozwiazanie_przed = Rozwiazanie_po_decyzji
            else:
                break
        tabela_cmax[i][a] = Cmax
tabela_sr = [0, 0]
for a in range(0, 2):
    for i in range(0, 30):
        tabela_sr[a] += tabela_cmax[i][a]


for i in range(0, 2):
    tabela_sr[i] = tabela_sr[i]/30
tabela_latex(tabela_cmax, tabela_sr)
