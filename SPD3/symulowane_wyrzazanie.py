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

    print('Wyrzazanie & Cmax & NEH & Cmax \\\\ \\hline')
    for i in tabela_cmax:
        print(
            f"--- & {i} & --- & {CmaxNEH}\\\\")
    print('\\hline')
    print(
        f"--- & {tabela_sr} & --- & {CmaxNEH}\\\\")
    print('\\hline\\hline')
    print('\\end{tabular}')


# przygotowanie danych
plik = "data.txt"
tabela, n, maszyny = przygotowanie_danych(plik)


# inicjalizacja algorytmu
tabela_cmax = []
Temperatura = 10
Wspolczynnik_schladzania = 0.99
Rozwiazanie_poczatkowe = [15, 225, 133, 43, 308, 11, 315, 136, 271, 244, 338, 405, 229, 261, 170, 149, 484, 108, 411, 105, 376, 395, 46, 245, 224, 286, 157, 446, 282, 485, 375, 359, 345, 452, 186, 305, 218, 435, 273, 110, 374, 243, 154, 249, 200, 113, 276, 414, 248, 147, 388, 167, 385, 365, 362, 55, 255, 42, 129, 24, 84, 3, 188, 409, 135, 486, 380, 331, 250, 310, 12, 389, 121, 277, 95, 377, 438, 203, 151, 393, 47, 44, 10, 126, 303, 481, 265, 364, 320, 28, 454, 73, 54, 220, 387, 307, 130, 115, 312, 30, 322, 169, 319, 437, 5, 141, 415, 433, 112, 464, 226, 445, 406, 237, 191, 187, 65, 379, 180, 212, 373, 193, 332, 232, 316, 453, 32, 174, 394, 210, 38, 287, 213, 124, 53, 290, 90, 422, 134, 190, 0, 21, 269, 219, 378, 214, 496, 171, 404, 80, 450, 27, 67, 391, 18, 127, 246, 398, 175, 296, 451, 9, 333, 142, 334, 313, 494, 66, 403, 421, 489, 295, 278, 4, 289, 34, 176, 469, 251, 236, 407, 222, 324, 216, 1, 74, 420, 473, 58, 241, 165, 465, 45, 201, 340, 128, 89, 41, 196, 140, 62, 107, 217, 293, 75, 372, 7, 91, 182, 152, 37, 148, 206, 462, 336, 270, 301, 51, 197, 76, 252, 361, 59, 284, 381, 330, 275, 194, 424, 164, 363, 272, 327, 339, 150, 457, 400, 488, 497, 288, 153, 35, 56, 29, 168, 300, 298, 482,
                          498, 235, 146, 397, 352, 425, 48, 474, 204, 264, 426, 370, 483, 408, 20, 390, 199, 36, 64, 88, 399, 460, 434, 297, 346, 448, 192, 268, 87, 137, 97, 357, 231, 63, 118, 184, 480, 19, 353, 233, 444, 342, 96, 69, 161, 173, 280, 162, 427, 384, 358, 306, 382, 160, 468, 6, 242, 493, 294, 215, 318, 470, 447, 274, 449, 443, 266, 131, 234, 26, 116, 22, 81, 103, 431, 109, 119, 429, 285, 442, 317, 79, 323, 279, 335, 329, 499, 253, 82, 16, 479, 17, 156, 172, 132, 122, 100, 155, 57, 328, 92, 383, 299, 402, 344, 195, 366, 477, 179, 292, 101, 343, 208, 159, 492, 354, 490, 123, 178, 77, 163, 144, 417, 230, 198, 125, 281, 355, 223, 78, 348, 8, 202, 302, 94, 227, 93, 491, 98, 456, 349, 466, 158, 392, 177, 347, 40, 99, 71, 371, 139, 33, 52, 259, 441, 117, 267, 418, 423, 221, 258, 487, 60, 257, 50, 238, 416, 360, 39, 455, 138, 209, 495, 86, 304, 367, 471, 143, 262, 72, 321, 205, 368, 189, 85, 463, 254, 283, 102, 419, 311, 239, 467, 428, 439, 31, 401, 2, 314, 183, 351, 247, 256, 410, 461, 120, 68, 263, 472, 13, 291, 211, 476, 185, 396, 458, 70, 356, 325, 166, 475, 309, 23, 436, 430, 260, 413, 111, 61, 337, 181, 326, 440, 341, 49, 114, 412, 350, 106, 145, 369, 104, 432, 478, 83, 207, 25, 228, 14, 240, 459, 386]
CmaxNEH = obliczenie_Cmax(Rozwiazanie_poczatkowe)
for i in range(0, 30):
    k = 0
    Rozwiazanie_przed = copy.deepcopy(Rozwiazanie_poczatkowe)
    Cmax = obliczenie_Cmax(Rozwiazanie_poczatkowe)
    # głowna petla programu
    Temperatura = 10
    kmax = 5000  # maksymalna ilosc iteracji
    TemperaturaMin = 1  # minimalna temperatura
    for k in range(0, kmax):  # kryterium stopu - liczba iteracji
        if Temperatura >= 1:  # kryterium stopu - temperatura graniczna
            Cmax_po = 99999
            Rozwiazanie_po = []
            for j in range(0, 5):
                Rozwiazanie_po_epoki = generowanie_ruchu_insert(Rozwiazanie_przed)
                Cmax_po_epoki = obliczenie_Cmax(Rozwiazanie_po_epoki)
                if Cmax_po_epoki < Cmax_po:
                    Cmax_po = Cmax_po_epoki
                    Rozwiazanie_po = Rozwiazanie_po_epoki
            # odrucenie rozwiazan z takim samym Cmax (modyfikacja)
            if Cmax_po != Cmax:
                Rozwiazanie_po_decyzji, Cmax = decyzja(
                    Cmax, Cmax_po, Rozwiazanie_po, Rozwiazanie_przed)
                Temperatura = schladzanie(Temperatura)
                Rozwiazanie_przed = Rozwiazanie_po_decyzji
        else:
            break

    tabela_cmax.append(Cmax)
tabela_sr = 0
for i in range(0, 30):
    tabela_sr += tabela_cmax[i]

tabela_sr /= 30
tabela_latex(tabela_cmax, tabela_sr)
