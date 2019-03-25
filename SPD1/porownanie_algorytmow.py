import itertools
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
    wartosci = odczyt(nazwa)
    tabela = []
    n = int(wartosci[0])
    ilosc = int(wartosci[1])
    for a in range(2, len(wartosci), ilosc):
        tabela_pomocnicza = []
        for b in range(0, ilosc):
            tabela_pomocnicza = tabela_pomocnicza+[wartosci[a+b]]
        tabela.append(tabela_pomocnicza)
    return tabela, n, ilosc


# funkcja zwracająca najmniejsza wartość w tablicy
def get_min_value(table):
    min_values = []
    for i in range(0, len(table)):
        min_value = min(table[i])
        min_values.append(min_value)

    return min(min_values)

# funkcja usuwająca zadanie z wartoscia czasu podana jako argument val


def remove_job(table, val):
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            if table[i][j] == val:
                for k in range(0, len(table[i])):
                    table[i][k] = 999
                return i, j


def Johnson2(tabela):
    lista = []
    for i in range(0, n):
        lista.append(0)
    j = 0
    k = 0
    for i in range(0, n):
        minval = get_min_value(tabela)
        removed = remove_job(tabela, minval)
        if removed[1] == 1:
            lista[n-1-j] = removed[0]
            j += 1
        else:
            lista[k] = removed[0]
            k += 1
    return lista

# sprowadzenie zadania 3 maszynowego do zadania 2 maszynowego


def obliczenie_Cmax(permutacja, ilosc):
    m = [0]*ilosc
    for i in permutacja:
        for j in range(0, ilosc):
            if j == 0:
                m[j] += tabela[i][j]
            else:
                m[j] = max(m[j], m[j-1])+tabela[i][j]
    return max(m)


def reduce_machines(table):
    reduced_table = []
    for i in range(0, len(table)):
        temp_table = []
        temp_table.append(table[i][0] + table[i][1])
        temp_table.append(table[i][1] + table[i][2])
        reduced_table.append(temp_table)
    return reduced_table


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


x = PrettyTable()
y = PrettyTable()
for i in range(5, 10):

    x.field_names = ["Algorytm Johnsona",
                     "Permutacja", "Czas wykonania", "Cmax"]
    plik = "3maszyny.txt"
    start = time.time_ns() / (10**9)
    tabela, n, ilosc = przygotowanie_danych(plik)
    if ilosc == 3:
        reduced_table = reduce_machines(tabela)
        lista = Johnson2(reduced_table)
    if ilosc == 2:
        lista = Johnson2(tabela)
    Cmax = obliczenie_Cmax(lista, ilosc)
    stop = time.time_ns() / (10**9)
    duration = stop - start
    x.add_row([i, lista, duration, Cmax])
    y.field_names = ["Przeglad zupelny",
                     "Permutacja", "Czas wykonania", "Cmax"]
    start = time.time_ns() / (10**9)
    tabela, n, ilosc = przygotowanie_danych(plik)
    permutacje, Cmax = przeglad_zupelny(n, ilosc, tabela)
    stop = time.time_ns() / (10**9)
    duration = stop - start
    y.add_row([i, permutacje[int(Cmax.index(min(Cmax)))], duration, min(Cmax)])

print(x)
print(y)


####################################################################################
