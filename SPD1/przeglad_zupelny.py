import itertools
import math
import time
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
    ilosc = int(Wartosci[1])
    for a in range(2, len(Wartosci), ilosc):
        tabela_pomocnicza = []
        for b in range(0, ilosc):
            tabela_pomocnicza = tabela_pomocnicza+[Wartosci[a+b]]
        tabela.append(tabela_pomocnicza)
    return tabela, n, ilosc


def przeglad_zupelny(n, ilosc, tabela):
    zakres = []
    for a in range(n):
        zakres.append(a)
    permutacje = list(itertools.permutations(zakres))
    Cmax = []
    for permutacja in permutacje:
        m = [0]*ilosc
        for i in permutacja:
            for j in range(0, ilosc):
                if j == 0:
                    m[j] += tabela[i][j]
                else:
                    m[j] = max(m[j], m[j-1])+tabela[i][j]
        Cmax.append(max(m))
    j = 0
    return permutacje, Cmax


def wypisanie_wynikow(Cmax, permutacje):
    a = int(Cmax.index(min(Cmax)))
    j = 0
    for i in permutacje:
        print(
            f"Dla kolejnosci {i} otrzymano czas na maszynach: {Cmax[j]}")
        j += 1
    print("-"*100)
    print(
        f"Dla kolejnosci {permutacje[a]} otrzymano optymalny czas na maszynach: {min(Cmax)}")


x = PrettyTable()
x.field_names = ["Brute Force", "Permutacja", "Czas wykonania", "Cmax"]
for i in range(5, 11):
    plik = "data\\"+str(i)+"data.txt"
    start = time.clock()
    tabela, n, ilosc = przygotowanie_danych(plik)
    permutacje, Cmax = przeglad_zupelny(n, ilosc, tabela)
    duration = time.clock() - start
    x.add_row([i, permutacje[int(Cmax.index(min(Cmax)))], duration, min(Cmax)])

print(x)
