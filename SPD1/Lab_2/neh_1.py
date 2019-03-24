import itertools
import math
import time
from prettytable import PrettyTable

# odczyt z pliku


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

# funkcja kluczujaca do sortowania tabeli


def sortSecond(val):
    return val[1]

# funkcja wyliczajaca Cmax poszczegolnych procesow i sortujaca Cmax malejaco, zwraca kolejnosc wykonywania operacji algorytmu neh


def sortowanie_tabeli(n, ilosc, tabela):
    sortownia = []
    kolejnosc = []

    for i in range(n):
        czas = 0
        for j in range(0, ilosc):
            czas += tabela[i][j]
        sortownia.append([i, czas])
    sortownia.sort(key=sortSecond, reverse=True)
    for i in sortownia:
        kolejnosc.append(i[0])
    return kolejnosc

# funkcja tworzaca permutacje do przegladu


def tworzenie_permutacji(wartosc, lista):
    permutacje = []
    for i in range(len(lista)+1):
        lista.insert(i, wartosc)
        permutacje.append(lista.copy())
        lista.pop(i)
    return permutacje

# funkcja wyliczajaca Cmax , zwraca kolejnosc z najkrotszym czasem i ten czas


def przeglad_zupelny(kolejnosc, ilosc, tabela):
    Cmax = []
    for permutacja in kolejnosc:
        m = [0]*ilosc
        for i in permutacja:
            for j in range(0, ilosc):
                if j == 0:
                    m[j] += tabela[i][j]
                else:
                    m[j] = max(m[j], m[j-1])+tabela[i][j]
        Cmax.append(max(m))
    n = Cmax.index(min(Cmax))
    najlepsza = kolejnosc[n]
    return najlepsza, min(Cmax)

# nie uzywana jesli uwazasz ze mozna to ja wywal


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


def utworz_graf(Pi, ilosc, tabela):
    graf = []
    for i in Pi:
        graf.append(tabela[i])
    print(graf)
    obciazenie = []
    for i in range(0, len(graf)):
        if i == 0:
            temp = []
            for j in range(0, ilosc):
                if j == 0:
                    temp = temp + [graf[i][j]]
                    obciazenie.append(temp)
                else:
                    temp = temp + [obciazenie[i][j-1] + graf[i][j]]
            obciazenie.append(temp)
            print(obciazenie)
        else:
            temp = []
            for j in range(0, ilosc):
                if j == 0:
                    temp = temp + [obciazenie[i-1][j] + graf[i][j]]
                else:
                    temp = temp + max([obciazenie[i-1][j], obciazenie[i][j-1]]) + graf[i][j]
            obciazenie.append(temp)
            print(obciazenie)

# GLOWNY KOD
plik = "data.txt"
tabela, n, ilosc = przygotowanie_danych(plik)
print(tabela)
start = time.time_ns() / (10**9)
kolejnosc = sortowanie_tabeli(n, ilosc, tabela)
najlepsza_kolejnosc = []
x = PrettyTable()
x.field_names = ["Permutacja", "Cmax", "Czas wykonywania"]
for i in kolejnosc:

    permutacje = tworzenie_permutacji(i, najlepsza_kolejnosc)
    najlepsza_kolejnosc, Cmax = przeglad_zupelny(permutacje, ilosc, tabela)
    G = utworz_graf(najlepsza_kolejnosc,ilosc,tabela)
duration = time.time_ns() / (10**9) - start
x.add_row([najlepsza_kolejnosc, Cmax, duration])
print(x)
