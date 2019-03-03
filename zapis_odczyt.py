import operator
TABLICA_RPQ = []
i = 0
r = 20
p = 5
q = 1


def zapisywanie_do_listy(r, p, q):
    tablica_pomocnicza = [int(r), int(p), int(q)]
    global TABLICA_RPQ
    global i
    TABLICA_RPQ = TABLICA_RPQ + [0]
    TABLICA_RPQ[i] = tablica_pomocnicza
    i += 1


def wypisywanie_z_listy():
    print("Wypisywanie wierszy po kolej")
    for a in TABLICA_RPQ:
        print(a)


for j in range(1, 10):
    # r = input("Podaj wartość r: ")
    # p = input("Podaj wartość p: ")
    # q = input("Podaj wartość q: ")

    zapisywanie_do_listy(r, p, q)
    r -= 2
    q += 2

wypisywanie_z_listy()
