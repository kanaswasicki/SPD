import itertools
import math

# funkcja odczytująca wartości z pliku tekstowego
def odczyt():
    theFile = open("3maszyny.txt", "r")
    theFloats = []
    for val in theFile.read().split():
        theFloats.append(float(val))
    theFile.close()
    return theFloats

def get_min_value(table):
    min_values = []
    for i in range(0, len(table)):
        min_value = min(table[i])
        min_values.append(min_value)

    return min(min_values)


def remove_job(table, val):
    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            if table[i][j] == val:
                for k in range(0, len(table[i])):
                    table[i][k] = 999
                return i, j


# sprowadzenie zadania 3 maszynowego do zadania 2 maszynowego
def reduce_machines(table):
    reduced_table = []
    for i in range(0,len(table)):
        temp_table = []
        temp_table.append(table[i][0] + table[i][1])
        temp_table.append(table[i][1] + table[i][2])
        reduced_table.append(temp_table)
    return reduced_table


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


reduced_table = reduce_machines(tabela)
lista = []
for i in range(0, n):
    lista.append(0)

j = 0
k = 0
for i in range(0, n):
    minval = get_min_value(reduced_table)
    removed = remove_job(reduced_table, minval)
    if removed[1] == 1:
        lista[n-1-j] = removed[0]
        j += 1
    else:
        lista[k] = removed[0]
        k += 1

print(lista)