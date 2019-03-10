import itertools
import math

# funkcja odczytująca wartości z pliku tekstowego


def odczyt():
    theFile = open("2maszyny.txt", "r")
    theFloats = []
    for val in theFile.read().split():
        theFloats.append(float(val))
    theFile.close()
    return theFloats

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

# segregowanie wartosci do pozniejszego wykorzystania w algorytmie
Wartosci = odczyt()
tabela = []
n = int(Wartosci[0])
ilosc = int(Wartosci[1])
for a in range(2, len(Wartosci), ilosc):
    tabela_pomocnicza = []
    for b in range(0, ilosc):
        tabela_pomocnicza = tabela_pomocnicza+[Wartosci[a+b]]
    tabela.append(tabela_pomocnicza)



# zastosowanie algorytmu Johnsona dla 2 maszyn

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

print(lista)