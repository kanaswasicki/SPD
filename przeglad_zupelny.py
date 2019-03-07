import itertools
import math

# funckja odczytująca wartości z pliku tekstowego


def odczyt():
    theFile = open("data.txt", "r")
    theInts = []
    for val in theFile.read().split():
        theInts.append(int(val))
    theFile.close()
    return theInts


# segregowanie wartosci do pozniejszego wykorzystania w algorytmie
Wartosci = odczyt()
tabela = []
n = Wartosci[0]
ilosc = Wartosci[1]
for a in range(2, len(Wartosci), ilosc):
    tabela_pomocnicza = []
    for b in range(0, ilosc):
        tabela_pomocnicza = tabela_pomocnicza+[Wartosci[a+b]]
    tabela.append(tabela_pomocnicza)

# wypisanie wszystkich permutacji
zakres = []
for a in range(n):
    zakres.append(a)
permutacje = list(itertools.permutations(zakres))
Cmax = [0]*math.factorial(n)
kolejnosc = 0
# korzystanie z przegladu zupelnego do obliczenia wartosci minimalnej
for permutacja in permutacje:
    m = [0]*ilosc
    for i in permutacja:
        for j in range(0, ilosc):
            if j == 0:
                m[j] += tabela[i][j]
            else:
                m[j] = max(m[j], m[j-1])+tabela[i][j]
    Cmax[kolejnosc] = max(m)
    kolejnosc += 1
a = int(Cmax.index(min(Cmax)))

print(
    f"Dla kolejnosci {permutacje[a]} otrzymano optymalny czas na maszynach: {min(Cmax)}")
