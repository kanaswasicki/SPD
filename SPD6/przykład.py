from __future__ import print_function
import collections
from ortools.sat.python import cp_model
import wczytywanie_danych

def Jobshop():
    "Problem job_shop"
    model = cp_model.CpModel()

    lista_prac = wczytywanie_danych.przygotowanie_danych('data1.txt')

    liczba_maszyn = 1 + max(zadanie[0] for praca in lista_prac for zadanie in praca)
    zakres_maszyn = range(liczba_maszyn)

    #wyliczanie maksymalnej możliwej wartości Cmax poprzez dodawanie wszystkich czasów
    horyzont = sum(zadanie[1] for praca in lista_prac for zadanie in praca)

    # Nazwany tuple do przechowywania wszystkich zadań
    typ_zadania = collections.namedtuple('typ_zadania', 'poczatek koniec interwal')
    # Nazwany tuple żeby manipulować informacjami rozwiązania (wykorzystane do wyświetlania danych)
    typ_zadania_wyswietlanie = collections.namedtuple('typ_zadania_wyswietlanie',
                                                'poczatek praca index czas_trwania')

    #Wpisanie poszczególnych zadanie'ów do tuple all_zadanie i dodanie do powiązanej listy maszyn
    wszystkie_zadania = {}
    lista_zadan_do_maszyny = collections.defaultdict(list)

    for praca_id, praca in enumerate(lista_prac):
        for zadanie_id, zadanie in enumerate(praca):
            maszyna = zadanie[0]
            czas_trwania = zadanie[1]
            suffix = '_%i_%i' % (praca_id, zadanie_id)
            start_var = model.NewIntVar(0, horyzont, 'poczatek' + suffix)
            end_var = model.NewIntVar(0, horyzont, 'koniec' + suffix)
            interval_var = model.NewIntervalVar(start_var, czas_trwania, end_var,
                                                'interwal' + suffix)
            wszystkie_zadania[praca_id, zadanie_id] = typ_zadania(
                poczatek=start_var, koniec=end_var, interwal=interval_var)
            lista_zadan_do_maszyny[maszyna].append(interval_var)

    # Dodanie constraina odpowiadającego za to żeby nie było możliwości wykonywania się 2 zadań na jednej maszynie w tym samym czasie
    for maszyna in zakres_maszyn:
        model.AddNoOverlap(lista_zadan_do_maszyny[maszyna])

    # Dodanie constraina odpowiadajacego za to, żeby nie było możliwości aby zadanie kolejne w ramach jednego praca'a zaczęło się szybciej niż poprzednie się skończyło
    for praca_id, praca in enumerate(lista_prac):
        for zadanie_id in range(len(praca) - 1):
            model.Add(wszystkie_zadania[praca_id, zadanie_id +
                                1].poczatek >= wszystkie_zadania[praca_id, zadanie_id].koniec)

    # zdefiniowanie problem Cmax jest wartościa maksymalna z zakonczonych zadan
    Cmax = model.NewIntVar(0, horyzont, 'makespan')
    model.AddMaxEquality(Cmax, [
        wszystkie_zadania[praca_id, len(praca) - 1].koniec
        for praca_id, praca in enumerate(lista_prac)
    ])
    # ustawienie constraina na Cmax (finalnego) odpowiadajacego za minimalizacje wartosci Cmax problemu job_shop
    model.Minimize(Cmax)

    # wywolanie modelu i rozwiazania
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        # Stworzenie listy zadan przypisanych do danej maszyny
        przypisane_zadanie = collections.defaultdict(list)
        for praca_id, praca in enumerate(lista_prac):
            for zadanie_id, zadanie in enumerate(praca):
                maszyna = zadanie[0]
                przypisane_zadanie[maszyna].append(
                    typ_zadania_wyswietlanie(
                        poczatek=solver.Value(wszystkie_zadania[praca_id, zadanie_id].poczatek),
                        praca=praca_id,
                        index=zadanie_id,
                        czas_trwania=zadanie[1]))

        # Stworzenie linii tekstu dla poszczegolnej maszyny
        wyswietlanie = ''
        for maszyna in zakres_maszyn:
            # Sortowanie po wartosciach poczatkowych
            przypisane_zadanie[maszyna].sort()
            wiersz_wykonanych_zadan = 'Maszyna ' + str(maszyna) + ': '
            wiersz_poczatek_koniec = '           '

            for zadanie in przypisane_zadanie[maszyna]:
                nazwa = 'zadanie_%i' % (zadanie.praca*4+zadanie.index+1)
                # dodanie spacji do stringa wyswietlanie zeby wyrownac kolumny
                wiersz_wykonanych_zadan += '%-20s' % nazwa

                poczatek = zadanie.poczatek
                czas_trwania = zadanie.czas_trwania
                temp_wiersz = '[%i,%i]' % (poczatek, poczatek + czas_trwania)
                # dodanie spacji do stringa wyswietlanie zeby wyrownac kolumny
                wiersz_poczatek_koniec += '%-20s' % temp_wiersz

            wiersz_poczatek_koniec += '\n'
            wiersz_wykonanych_zadan += '\n'
            wyswietlanie += wiersz_wykonanych_zadan
            wyswietlanie += wiersz_poczatek_koniec

        # Printowanie wyniku programu solver metoda CP
        print('Optymalna długość uszeregowania: %i' % solver.ObjectiveValue())
        print(wyswietlanie)


Jobshop()

