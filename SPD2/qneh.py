import itertools
import math
import copy
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
            tabela_pomocnicza = tabela_pomocnicza + [Wartosci[a + b]]
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
    for i in range(len(lista) + 1):
        lista.insert(i, wartosc)
        permutacje.append(lista.copy())
        lista.pop(i)
    return permutacje


# funkcja wyliczajaca Cmax , zwraca kolejnosc z najkrotszym czasem i ten czas


def przeglad_zupelny(kolejnosc, ilosc, tabela):
    Cmax = []
    for permutacja in kolejnosc:
        m = [0] * ilosc
        for i in permutacja:
            for j in range(0, ilosc):
                if j == 0:
                    m[j] += tabela[i][j]
                else:
                    m[j] = max(m[j], m[j - 1]) + tabela[i][j]
        Cmax.append(max(m))
    n = Cmax.index(min(Cmax))
    najlepsza = kolejnosc[n]
    return najlepsza, min(Cmax)


# nie uzywana jesli uwazasz ze mozna to ja wywal


def utworz_graf(Pi, ilosc, tabela):
    graf = []
    for i in Pi:
        graf.append(tabela[i])
    obciazenie = []
    for k in range(len(graf)):
        obciazenie.append([0] * ilosc)

    for i in range(0, len(graf)):
        if i == 0:
            for j in range(0, ilosc):
                if j == 0:
                    obciazenie[i][j] = graf[i][j]
                else:
                    obciazenie[i][j] = obciazenie[i][j - 1] + graf[i][j]
        else:
            for j in range(0, ilosc):
                if j == 0:
                    obciazenie[i][j] = obciazenie[i - 1][j] + graf[i][j]
                else:
                    obciazenie[i][j] = max([obciazenie[i - 1][j], obciazenie[i][j - 1]]) + graf[i][j]
    #################################################################
    # print(obciazenie)
    # obciazenie = []
    # for i in range(0, len(graf)):
    #    m = 0
    #    obciazenie_linii = []
    #    for j in range(0, ilosc):
    #        if i == 0:
    #            m += graf[i][j]
    #            obciazenie_linii.extend([m])
    #        elif i == 1:
    #            m = max(m, obciazenie[i - 1][j]) + graf[i][j]
    #            obciazenie_linii.extend([m])
    #        else:
    #            m = max(obciazenie[i - 1][j], m) + graf[i][j]
    #            obciazenie_linii.extend([m])
    #    obciazenie.append(obciazenie_linii)
    ##################################################################
    i = 0;
    j = 0;
    sciezka = []
    while (i != len(graf) - 1) or (j != ilosc - 1):
        if obciazenie[len(graf) - i - 1][ilosc - j - 1] - graf[len(graf) - i - 1][ilosc - j - 1] == \
                obciazenie[len(graf) - i - 2][ilosc - j - 1]:
            sciezka.append([len(graf) - i - 1, ilosc - j - 1])
            i = i + 1

        elif obciazenie[len(graf) - i - 1][ilosc - j - 1] - graf[len(graf) - i - 1][ilosc - j - 1] == \
                obciazenie[len(graf) - i - 1][ilosc - j - 2]:
            sciezka.append([len(graf) - i - 1, ilosc - j - 1])
            j = j + 1
    sciezka.append([0, 0])
    return sciezka, graf, obciazenie


def utworz_graf2(Pi, ilosc, tabela):
    graf = []
    for i in Pi:
        graf.append(tabela[i])
    obciazenie = []
    for k in range(len(graf)):
        obciazenie.append([0] * ilosc)

    for i in range(1, len(graf) + 1):
        if i == 0:
            for j in range(1, ilosc + 1):
                if j == 0:
                    obciazenie[-i][-j] = graf[-i][-j]
                else:
                    obciazenie[-i][-j] = obciazenie[-i][-j + 1] + graf[-i][-j]
        else:
            for j in range(1, ilosc + 1):
                if j == 0:
                    obciazenie[-i][-j] = obciazenie[-i + 1][-j] + graf[-i][-j]
                else:
                    obciazenie[-i][-j] = max([obciazenie[-i + 1][-j], obciazenie[-i][-j + 1]]) + graf[-i][-j]
    return obciazenie
# Akceleracja polega na tym, że tylko raz musimy przejsc przez cala macierz m x n przy wstawianiu zadania
# przechodzimy przez macierz wyliczając obciazenie1 i obciazenie2, a sprawdzanie wszystkich uszeregowan dokonujemy na
# obliczonych macierzach, wyznaczając zawsze tylko jeden dodatkowy wektor dla każdej pozycji
#
# przyklad:
# mamy uszeregowanie z poprzedniego kroku [9, 18, 7];
# chcac wstawic kolejne zadanie '3' przeprowadzamy nastepujace kroki:
# rozwazamy 4 mozliwe pozycje [9, 3, 18, 7]; [9, 18, 3, 7]; [9, 18, 3, 7]; [9, 18, 7, 3];
# i = 0
# krok 1:
# obliczamy jakie wartosci obciazen1 miałoby zadanie w pozycji i, wpisujemy do wektora temp
# krok 2:
# sumujemy obciazenie1 naszego zadania z obciazeniem2 zadania nastepnego w uszeregowaniu
# dostajemy wektor C rozmiaru m-ilosc maszyn
# krok 3:
# wybieramy wartosc najwieksza, co daje nam pewnosc ze zawarlismy krok ze sciezka krytyczna
# krok 4:
# i+=1 , przjescie do kroku 1, gdy i < n+1
# Krok ostatni:
# wybór uszeregowania dla którego Cmax przyjmuje wartosc najmniejsza
def neh_akceleracja(kolejnosc, obciazenie1, obciazenie2, tabela, element):
    Cmax = [] # lista 1x(n+1) przygotowana dla Cmax z kazdego uszeregowania
    for i in range(len(obciazenie2) + 1):
        #szukając pozycji 4 elementu w uszeregowaniu, musimy rozważyć dla niego 4 pozycje
        # na poczatku, na koncu i pomiedzy poprzednimi zadaniami
        # ilosc mozliwych pozycji nowego elementu = n + 1, len(obciazenie2) + 1
        # n - ilosc zadan w dodtychczasowym najlepszym uszeregowaniu
        # m - ilosc maszyn

        temp = [] #(rozmiar m) lista tymczasowa, która przechowuje wartosci obciazenia1, gdybyśmy zadanie wstawili w wybrane miejsce
        C = [] #(rozmiar m)  lista zawierająca obciazenia kazdej ze sciezek w konkretnym uszeregowaniu( slajd 10).

        if i == 0:
        # rozważenie przypadku wstawiania elementu przed wszystkie poprzednie zadania (na początek uszeregowania)

            for j in range(len(tabela[element])):
                # w wybranym uszeregowaniu (tutaj na 0 pozycji i==0) wyznaczamy wage/obciazenie  tego zadana w przypadku gdyby
                # znajdował sie na tej pozycji (wedlug zasady jak w obciazenie1), czyli obciazenie prawostronne
                # wyznaczamy obciazenia dla kazdej maszyny wchodzacej w to zadanie i zapisujemy w liscie temp
                # m = len(tabela[element] - ilosc maszyn

                if j == 0:                 # przypadek rozwazajacy obciazenie 0 maszyny na zerowej pozycji zadania

                    temp.append(tabela[element][j])             # dodawanie wyliczonego obciazenia maszyny w zadaniu do listy
                else:                               # przypadek rozwazajacy obciazenie pozostałych maszyn na 0 pozycji zadania
                    temp.append(tabela[element][j] + temp[j - 1])# dodawanie wyliczonego obciazenia maszyny w zadaniu do listy

                C.append(temp[j] + obciazenie2[i][j])   # zsumowane wyliczone obciązenie 'prawostronne' maszyny j w uszeregowaniu na pozycji i
                #                                                         # z obciazeniem lewostronnym zadania które w tym uszeregowaniu wystepowałoby po nim
            Cmax.append(max(C))    # Cmax tego uszeregowania wyznaczany jako max(C), ponieważ musimy wybrać sciezke krytyczna (slajd 10)

        elif i == len(obciazenie2):
        # rozważenie przypadku wstawiania elementu za wszystkie zadania ( na koniec)

            for j in range(len(tabela[element])):
                # w wybranym uszeregowaniu (tutaj na ostatniej pozycji pozycji len(obciazenie2)) wyznaczamy wage/obciazenie  tego zadana w przypadku gdyby
                # znajdował sie na tej pozycji (wedlug zasady jak w obciazenie1), czyli obciazenie prawostronne
                # wyznaczamy obciazenia dla kazdej maszyny wchodzacej w to zadanie i zapisujemy w liscie temp
                # m = len(tabela[element] - ilosc maszyn

                if j == 0:# przypadek rozwazajacy obciazenie 0 maszyny na ostatniej  pozycji zadania

                    temp.append(tabela[element][j] + obciazenie1[i - 1][j])
                    # dodawanie wyliczonego obciazenia maszyny w zadaniu do listy
                    # obciazenie prawostronne w tym uszeregowaniu dla maszyny 0 w pozycji zadania i(na koncu) liczymy dodajac do czasu pracy
                    # na maszynie j=0 obciazenie1 z maszyny j=0 zadania i-1
                else:
                    temp.append(tabela[element][j] + max(obciazenie1[i - 1][j], temp[j - 1]))
                    # obciazenie prawostronne w tym uszeregowaniu dla maszyny j w pozycji zadania i(na koncu) liczymy
                    # dodajac do czasu pracy na maszynie j obciazenie1 z maszyny i-1
                C.append(temp[j])# wyliczone obciązenie 'prawostronne' maszyny j dodajemy do listy C. Zadanie rozpartrujemy na ostatniej pozycji
                                 # wiec nie dodajemy zadania wystepujacego po nim
            Cmax.append(max(C))  # Cmax tego uszeregowania wyznaczany jako max(C), ponieważ musimy wybrać sciezke krytyczna (slajd 10)
        else:
      # rozważenie przypadku wstawiania elementu w srodek uszeregowania

            for j in range(len(tabela[element])):
                # w wybranym uszeregowaniu (tutaj w seodu uszeregowania) wyznaczamy wage/obciazenie  tego zadana w przypadku gdyby
                # znajdował sie na tej pozycji (wedlug zasady jak w obciazenie1), czyli obciazenie prawostronne
                # wyznaczamy obciazenia dla kazdej maszyny wchodzacej w to zadanie i zapisujemy w liscie temp
                # m = len(tabela[element] - ilosc maszyn

                if j == 0:#przypadek rozwazajacy obciazenie 0 maszyny w pozycji zadania w srodku uszeregowania

                    temp.append(tabela[element][j] + obciazenie1[i - 1][j])
                    # dodawanie wyliczonego obciazenia maszyny w zadaniu do listy
                    # obciazenie prawostronne w tym uszeregowaniu dla maszyny 0 w pozycji zadania i(w srodku) liczymy dodajac do czasu pracy
                    # na maszynie j=0 obciazenie1 z maszyny j=0 zadania i-1
                else:
                    temp.append(tabela[element][j] + max(obciazenie1[i - 1][j], temp[j - 1]))
                    # obciazenie prawostronne w tym uszeregowaniu dla maszyny j w pozycji zadania i(w srodu) liczymy
                    # dodajac do czasu pracy na maszynie j obciazenie1 z maszyny i-1
                C.append(temp[j] + obciazenie2[i][j])# zsumowane wyliczone obciązenie 'prawostronne' maszyny j w uszeregowaniu na pozycji i
                                                     # z obciazeniem lewostronnym zadania które w tym uszeregowaniu wystepowałoby po nim
            Cmax.append(max(C))# Cmax tego uszeregowania wyznaczany jako max(C), ponieważ musimy wybrać sciezke krytyczna (slajd 10)
    miejsce = Cmax.index(min(Cmax)) # mając Cmax dla kazdego uszeregowwania wybieramy to najlepsze, bierzemy jego i przypisujemy jako miejsce gdzie nalezy wstawic
                                    # np wstawiajac 4 zadanie mamy mozliwe miejsce 0,1,2,3
    kolejnosc.insert(miejsce, element)#wstawiamy element w wybrane miejsce
    return kolejnosc, min(Cmax)
#


# GLOWNY KOD

x = PrettyTable()
k = 0
x.field_names = ["QNEH", "Cmax", "Czas wykonywania"]

najlepsza_kolejnosc = []
plik = "data.txt"
tabela, n, ilosc = przygotowanie_danych(plik)
start = time.time_ns() / (10 ** 9)
kolejnosc = sortowanie_tabeli(n, ilosc, tabela)
for i in kolejnosc:
    if k == 0:
        permutacje = tworzenie_permutacji(i, najlepsza_kolejnosc)
        najlepsza_kolejnosc, Cmax = przeglad_zupelny(permutacje, ilosc, tabela)
        k += 1
    else:
        najlepsza_kolejnosc, Cmax = neh_akceleracja(najlepsza_kolejnosc, obciazenie, obciazenie2, tabela, i)
    sciezka, graf, obciazenie = utworz_graf(najlepsza_kolejnosc, ilosc, tabela)
    obciazenie2 = utworz_graf2(najlepsza_kolejnosc, ilosc, tabela)
duration = time.time_ns() / (10 ** 9) - start
x.add_row(["-", Cmax, duration])

print(x)
