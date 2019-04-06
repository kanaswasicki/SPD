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
def inicjalizacja(ilosc_zadan, temperatura, wspolczynnik):
    lista = list(range(0, ilosc_zadan))
    random.shuffle(lista)
    return lista, temperatura, wspolczynnik


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
    else: #rozpisane tak dokładnie aby istniala mozliwosc sledzenia wartosci prawdopodobienstwa w debuggerze
        p = math.exp((cmax_po-cmax_przed)/Temperatura)
        prand = random.random()
        if p >= prand:
            return rozwiazanie_po, cmax_po
        else:
            return rozwiazanie_przed, cmax_przed


# alternatywna funkcja decyzyjna, nie dajemy 1 dla lepszych rozwiazan
def decyzja_mod(cmax_przed, cmax_po,  rozwiazanie_po, rozwiazanie_przed):

    p = math.exp((cmax_po-cmax_przed)/Temperatura)
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



'''
wersja podstawowa:
    inicjalizacja
    for
        generwoanie ruchu swap
        obliczenie cmax
        decyzja
        schladzanie
        
modyfikacja 1:
    wybranie najlepszego naszego algorytmu i porownanie z neh
    (zrobic na koniec, gdy dobierzemy parametry)

modyfikacja 2:
    inicjalizacja
    for
        generwoanie ruchu swap / insert - porownanie
        obliczenie cmax
        decyzja
        schladzanie
    
modyfikacja 3:
    inicjalizacja -zmiana parametru schladzania i porowanie
    for
        generwoanie ruchu swap 
        obliczenie cmax
        decyzja
        schladzanie
        
modyfikacja 4:
dobor temperatur LUB inny sposob schladzania 
    inicjalizacja -zmiana temp poczatkowej
    for (zmiana temp koncowej)
        generwoanie ruchu swap 
        obliczenie cmax
        decyzja
        schladzanie/schladzanie2 -porownac
        
modyfikacja 5:
    inicjalizacja
    for 
        generwoanie ruchu swap 
        obliczenie cmax
        decyzja_mod
        schladzanie
        
modyfikacja 6:

    inicjalizacja
    for (z odrzucaniem takich samych Cmax i bez, porownac. Wersja bez jest na koncu kodu, zakomentowana)
        generwoanie ruchu swap 
        obliczenie cmax
        decyzja_mod
        schladzanie

modyfikacja 7:
    inicjalizacja vs inicjalizacja + Rozwiazanie_poczatkowe = NEH
    for 
        generwoanie ruchu swap 
        obliczenie cmax
        decyzja_mod
        schladzanie

modyfikacja 8:
    Jeszcze nie mam pomysłu
    
    DODATKOWO DO WSZYSTKICH MODYFIKACJI MOZNA UZYWAC INNYCH FUNKCJI (NP INSERT ZAMIAST SWAP, WAZNE ZEBY POROWNUJAC ZMIENAC TYLKO JEDEN ELEMENT)
    NA KONIEC STWORZYC NAJELPSZE ROZWIAZANIE I WYKONAC MODYFIKACJE 1.
'''
## przygotowanie danych
plik = "data.txt"
tabela, n, maszyny = przygotowanie_danych(plik)


## inicjalizacja algorytmu
Rozwiazanie_poczatkowe, Temperatura, Wspolczynnik_schladzania = inicjalizacja(n, 20000, 0.9)
Cmax = obliczenie_Cmax(Rozwiazanie_poczatkowe)
Rozwiazanie_przed = Rozwiazanie_poczatkowe

# głowna petla programu
kmax = 50000;           #maksymalna ilosc iteracji
TemperaturaMin = 1      #minimalna temperatura
for k in range(0, kmax): #kryterium stopu - liczba iteracji
    if Temperatura >= 1: #kryterium stopu - temperatura graniczna
        Rozwiazanie_po = generowanie_ruchu_insert(Rozwiazanie_przed)
        Cmax_po = obliczenie_Cmax(Rozwiazanie_po)

        if Cmax_po != Cmax: # odrucenie rozwiazan z takim samym Cmax (modyfikacja)
            Rozwiazanie_po_decyzji, Cmax = decyzja(Cmax, Cmax_po, Rozwiazanie_po, Rozwiazanie_przed)
            Temperatura = schladzanie(Temperatura)
            Rozwiazanie_przed = Rozwiazanie_po_decyzji
    else:
        break
Rozwiazanie_koncowe = Rozwiazanie_przed
print(Rozwiazanie_koncowe, Cmax, Temperatura)

""" to samo co powyzej ale wersja bez odrzucania rozwiazan z takim samym cmax (bez modyfikacji)
kmax = 50000;
for k in range(0, kmax): #kryterium stopu - liczba iteracji
    if Temperatura >= 1: #kryterium stopu - temperatura graniczna
        Rozwiazanie_po = generowanie_ruchu_insert(Rozwiazanie_przed)
        Cmax_po = obliczenie_Cmax(Rozwiazanie_po)
        Rozwiazanie_po_decyzji, Cmax = decyzja(Cmax, Cmax_po, Rozwiazanie_po, Rozwiazanie_przed)
        Temperatura = schladzanie(Temperatura)
        Rozwiazanie_przed = Rozwiazanie_po_decyzji
    else:
        break
Rozwiazanie_koncowe = Rozwiazanie_przed
print(Rozwiazanie_koncowe, Cmax, Temperatura)
"""



"""
#### rozwiazanie dla kryterium stopu - temperatura graniczna####
temperatura_graniczna = 1;
while temperatura >= temperatura_graniczna:
    rozwiazanie_po = generowanie_ruchu_swap(rozwiazanie_przed)
    rozwiazanie_po_decyzji = decyzja(Cmax, rozwiazanie_po)
    temperatura = schladzanie(temperatura)
    rozwiazanie_przed = rozwiazanie_po_decyzji
rozwiazanie_koncowe = rozwiazanie_przed
print(rozwiazanie_koncowe, Cmax)
"""

"""
#### rozwiazanie dla kryterium stopu - liczba iteracji####
temperatura_graniczna = 1;
for k in range(0, kmax):
    rozwiazanie_po = generowanie_ruchu_swap(rozwiazanie_przed)
    rozwiazanie_po_decyzji = decyzja(Cmax, rozwiazanie_po)
    temperatura = schladzanie(temperatura)
    rozwiazanie_przed = rozwiazanie_po_decyzji
rozwiazanie_koncowe = rozwiazanie_przed
print(rozwiazanie_koncowe, Cmax)
"""