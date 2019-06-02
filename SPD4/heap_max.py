import math


def heap_parent(n):
    if n != 0:
        return math.floor((n - 1) / 2)
    else:
        return 0


def heap_left(n):
    return (2 * n + 1)


def heap_right(n):
    return (2 * n + 2)


def swap(L, left, right):
    # L[left], L[right] = L[right], L[left]
    item = L[left]
    L[left] = L[right]
    L[right] = item


# Naprawa kopca, gdy na pozycji ipos zwiększył się priorytet.
def fix_up(L, ipos, kolumna):
    ppos = heap_parent(ipos)
    # tu widać, że korzeń ma nr 0
    while (ipos > 0) and (L[ppos][kolumna] < L[ipos][kolumna]):
        swap(L, ppos, ipos)
        # przesunięcie węzła w górę
        ipos = ppos
        ppos = heap_parent(ipos)


# Naprawa kopca, gdy na pozycji ipos zmniejszył się priorytet.
def fix_down(L, ipos, n, kolumna):
    # n - rozmiar tablicy, nie możemy przekroczyć
    # UWAGA indeksy tablicy są mniejsze od n
    while True:
        # wybór dziecka do zamiany z bieżącym węzłem
        lpos = heap_left(ipos)
        rpos = heap_right(ipos)
        if lpos < n and L[lpos][kolumna] > L[ipos][kolumna]:
            mpos = lpos
        else:
            mpos = ipos
        if rpos < n and L[rpos][kolumna] > L[mpos][kolumna]:
            mpos = rpos
        if mpos == ipos:
            break  # drzewo to sterta
        else:  # trzeba zamienić z dzieckiem
            swap(L, mpos, ipos)
            # przesuwam węzeł o jeden poziom w dół
            ipos = mpos


class Heap_max:
    """Implementacja sterty (kopca max)."""

    def __init__(self, kolumna):
        self.items = []  # tu trzymamy elementy sterty
        self.kolumn = kolumna

    def __str__(self):  # podglądamy stertę
        return str(self.items)

    def is_empty(self):
        return not self.items

    def insert(self, item):  # nie zwraca wartości
        self.items.append(item)  # dodajemy na koniec tablicy
        # ponowne przekształcenie drzewa w stertę
        fix_up(self.items, len(self.items) - 1, self.kolumn)

    def remove(self):  # zwraca element największy
        k = len(self.items) - 1
        # najpierw największy na koniec
        swap(self.items, 0, k)
        # trzeba poprawić drzewo, zaczynam od góry
        # znowu widać, że zaczynam od korzenia nr 0
        fix_down(self.items, 0, k, self.kolumn)
        return self.items.pop()

    def count(self):  # liczba elementów na stercie
        return len(self.items)
