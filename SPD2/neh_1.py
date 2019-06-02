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
    i = 0
    j = 0
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


def neh_mod1(sciezka, graf, i, kolejnosc):
    max = 0;
    index = 999;
    zadanie_odrzucone = 999
    for k in range(len(kolejnosc)):
        if i == kolejnosc[k]:
            zadanie_odrzucone = k
    for i in sciezka:
        if i[0] != zadanie_odrzucone:
            if graf[i[0]][i[1]] > max:
                max = graf[i[0]][i[1]]
                index = i[0]
    if index == 999:
        return -1
    return kolejnosc[index]


def neh_akceleracja(kolejnosc, obciazenie1, obciazenie2, tabela, element):
    Cmax = []
    for i in range(len(obciazenie2) + 1):
        temp = []
        C = []
        if i == 0:
            for j in range(len(tabela[element])):
                if j == 0:
                    temp.append(tabela[element][j])
                else:
                    temp.append(tabela[element][j] + temp[j - 1])
                C.append(temp[j] + obciazenie2[i][j])
            Cmax.append(max(C))
        elif i == len(obciazenie2):
            for j in range(len(tabela[element])):
                if j == 0:
                    temp.append(tabela[element][j] + obciazenie1[i - 1][j])
                else:
                    temp.append(tabela[element][j] + max(obciazenie1[i - 1][j], temp[j - 1]))
                C.append(temp[j])
            Cmax.append(max(C))
        else:
            for j in range(len(tabela[element])):
                if j == 0:
                    temp.append(tabela[element][j] + obciazenie1[i - 1][j])
                else:
                    temp.append(tabela[element][j] + max(obciazenie1[i - 1][j], temp[j - 1]))
                C.append(temp[j] + obciazenie2[i][j])
            Cmax.append(max(C))
    miejsce = Cmax.index(min(Cmax))
    kolejnosc.insert(miejsce, element)
    return kolejnosc, min(Cmax)


# GLOWNY KOD

x = PrettyTable()

x.field_names = ["QNEH mod 1", "Cmax", "Czas wykonywania"]
k = 0
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
        sciezka, graf, obciazenie = utworz_graf(najlepsza_kolejnosc, ilosc, tabela)
        obciazenie2 = utworz_graf2(najlepsza_kolejnosc, ilosc, tabela)
        najlepsza_kolejnosc, Cmax = neh_akceleracja(najlepsza_kolejnosc, obciazenie, obciazenie2, tabela, i)

        X = neh_mod1(sciezka, graf, i, najlepsza_kolejnosc)
        if X != -1:
            najlepsza_kolejnosc.remove(X)
            sciezka, graf, obciazenie = utworz_graf(najlepsza_kolejnosc, ilosc, tabela)
            obciazenie2 = utworz_graf2(najlepsza_kolejnosc, ilosc, tabela)
            najlepsza_kolejnosc, Cmax = neh_akceleracja(najlepsza_kolejnosc, obciazenie, obciazenie2, tabela, X)

duration = time.time_ns() / (10 ** 9) - start
x.add_row(["-", Cmax, duration])
print(x)
