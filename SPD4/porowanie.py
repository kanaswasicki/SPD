import operator
import copy
import heap_min
import algorytm_schrage_heap as schrage
import time
import matplotlib.pyplot as plt
import symulowane_wyrzazanie as sym


def tabela_latex_Cmax(tabela_czas, tabela_in):
    print('\\begin{tabular}{|c|c|c|c|c|}')

    print('Lp. & Schrage & Schrageptmn & Schrage kopiec & Schrageptmn kopiec \\\\ \\hline')
    for i in range(0,len(tabela_in)):
        print(
            f" {tabela_in[i]}& {tabela_czas[i][0]} & {tabela_czas[i][1]} & {tabela_czas[i][2]} & {tabela_czas[i][3]}\\\\")
    print('\\hline\\hline')
    print('\\end{tabular}')
#funkcja do liczenia Cmax dla wyzarzania na 5.5. Tabela jest zwracana przez algorytm Schrage i Schrage z podzialem. Kolejnosc poczatkowa to [0,1,2,3,...,n] dodaj w odpowiednie miejsca te funkcje.



c = [[1513.0, 3076.0, 6416.0], [1492.0, 3070.0, 6398.0]]
tabela_czas = []
tabela_Cmax = []
tabela_in = []
tabela_czas_sr = []
tabela = []
ran = 10
tabela_cmax = []
Temperatura = 10
Wspolczynnik_schladzania = 0.99
im = [50,100,200]
#for a in range(10,10+ran):
 #   tabela_in.append(a)
#for i in range(10,20):
for a in range(0,10):
    for i in im:
            tmp_cmax = []
            plik = "in"+str(i)+".txt"
            tabela = schrage.przygotowanie_danych(plik)
            tabela_sym, Cmax = schrage.schrage(tabela)
            tmp_cmax.append(Cmax)

            kolejnosc = []
            for j in range(0, len(tabela)):
                kolejnosc.append(j)
            CmaxNEH = sym.obliczenie_Cmax(kolejnosc, tabela_sym)



            k = 0
            Rozwiazanie_przed = copy.deepcopy(kolejnosc)
            Cmax = sym.obliczenie_Cmax(kolejnosc, tabela_sym)
            # głowna petla programu
            Temperatura = 10
            kmax = 5000  # maksymalna ilosc iteracji
            TemperaturaMin = 1  # minimalna temperatura
            for k in range(0, kmax):  # kryterium stopu - liczba iteracji
                if Temperatura >= 1:  # kryterium stopu - temperatura graniczna
                    Cmax_po = 99999
                    Rozwiazanie_po = []
                    for j in range(0, 5):
                        Rozwiazanie_po_epoki = sym.generowanie_ruchu_insert(Rozwiazanie_przed)
                        Cmax_po_epoki = sym.obliczenie_Cmax(Rozwiazanie_po_epoki, tabela_sym)
                        if Cmax_po_epoki < Cmax_po:
                            Cmax_po = Cmax_po_epoki
                            Rozwiazanie_po = Rozwiazanie_po_epoki
                    # odrucenie rozwiazan z takim samym Cmax (modyfikacja)
                    if Cmax_po != Cmax:
                        Rozwiazanie_po_decyzji, Cmax = sym.decyzja(
                            Cmax, Cmax_po, Rozwiazanie_po, Rozwiazanie_przed)
                        Temperatura = sym.schladzanie(Temperatura)
                        Rozwiazanie_przed = Rozwiazanie_po_decyzji
                else:
                    break
            tmp_cmax.append(Cmax)
            tabela_cmax.append(tmp_cmax)

print(tabela_cmax)

#tabela_latex_Cmax(tabela_Cmax, tabela_in)
