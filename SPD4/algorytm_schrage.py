import operator
import copy
import heap_min
import algorytm_schrage_heap as schrage
import time
import matplotlib.pyplot as plt

def tabela_latex_czas(tabela_czas, tabela_in):
    print('\\begin{tabular}{|c|c|c|c|c|}')

    print('Lp. & Schrage & Schrageptmn & Schrage kopiec & Schrageptmn kopiec \\\\ \\hline')
    for i in range(0,len(tabela_czas[0])):
        print(
            f" {tabela_in[i]}& {tabela_czas[0][i]} & {tabela_czas[1][i]} & {tabela_czas[2][i]} & {tabela_czas[3][i]}\\\\")
    print('\\hline\\hline')
    print('\\end{tabular}')

def tabela_latex_Cmax(tabela_czas, tabela_in):
    print('\\begin{tabular}{|c|c|c|c|c|}')

    print('Lp. & Schrage & Schrageptmn & Schrage kopiec & Schrageptmn kopiec \\\\ \\hline')
    for i in range(0,len(tabela_in)):
        print(
            f" {tabela_in[i]}& {tabela_czas[i][0]} & {tabela_czas[i][1]} & {tabela_czas[i][2]} & {tabela_czas[i][3]}\\\\")
    print('\\hline\\hline')
    print('\\end{tabular}')
#funkcja do liczenia Cmax dla wyzarzania na 5.5. Tabela jest zwracana przez algorytm Schrage i Schrage z podzialem. Kolejnosc poczatkowa to [0,1,2,3,...,n] dodaj w odpowiednie miejsca te funkcje.

def liczCmax (kolejność, tabela):
  r = 0
  p = 0
  Cmax = 0
  for a in kolejność:
    r = tabela[a][0]
    p = max(p, tabela[a][0]) + tabela[a][1]
    Cmax = max(Cmax, p+tabela[a][2])
  return Cmax


kolejnosc = []
for i in range (0,len(tabela)):
  kolejnosc.append(i)

Cmax = liczCmax(kolejsc, tabela)


c = [[1513.0, 3076.0, 6416.0], [1492.0, 3070.0, 6398.0]]
tabela_czas = []
tabela_Cmax = []
tabela_in = []
tabela_czas_sr = []
tabela = []
ran = 490
for a in range(10,10+ran):
    tabela_in.append(a)
for b in range(1, 4):
    for i in range(10,10+ran):
        tmp_czas = []
        tmp_cmax = []
        plik = "data"+str(b)+"\\" + str(i)+"data.txt"

        #tabela = schrage.przygotowanie_danych(plik)
        #start1 = time.time_ns() / (10 ** 9)
       # for a in range(10):

        kolejnosc, Cmax = schrage.schrage(tabela)
       # tmp_czas.append(time.time_ns() / (10 ** 9) - start1)
       # tmp_cmax.append(Cmax)

       # tabela = schrage.przygotowanie_danych(plik)
      #  start2 = time.time_ns() / (10 ** 9)

       # for a in range(10):

       #     kolejnosc, Cmax = schrage.schragepmtn(tabela)
       # tmp_czas.append(time.time_ns() / (10 ** 9) - start2)
       # tmp_cmax.append(Cmax)

        tabela = heap_min.Heap_min(0)
        tabela = schrage.przygotowanie_danych_heap(plik, tabela)
        start3 = time.time_ns() / (10 ** 9)

        for a in range(10):

            kolejnosc, Cmax = schrage.schrage_heap(tabela)
        tmp_czas.append(time.time_ns() / (10 ** 9) - start3)
        tmp_cmax.append(Cmax)

        tabela = heap_min.Heap_min(0)
        tabela = schrage.przygotowanie_danych_heap(plik, tabela)
        start4 = time.time_ns() / (10 ** 9)

        for a in range(10):

            kolejnosc, Cmax = schrage.schragepmtn_heap(tabela)
        tmp_czas.append(time.time_ns() / (10 ** 9) - start4)
        tmp_cmax.append(Cmax)
        tabela_czas.append(tmp_czas)
        tabela_Cmax.append(tmp_cmax)


for j in range(0,2):
    tabela_tmp = []
    for i in range(0,ran):
        tabela_tmp.append((tabela_czas[i][j]+tabela_czas[i+ran][j]+tabela_czas[i+2*ran][j])/3)
    tabela_czas_sr.append(tabela_tmp)
    print(tabela_czas_sr)
#tabela_latex_czas(tabela_czas_sr, tabela_in)
#tabela_latex_Cmax(tabela_Cmax, tabela_in)
plt.xlabel('ilosc zadan')
plt.ylabel('czas')
tabela = []

line_3, =plt.plot(tabela_in, tabela_czas_sr[0], label = 'Schrage kopiec')
line_4, =plt.plot(tabela_in, tabela_czas_sr[1], label = 'Schrageptmn kopiec')
plt.legend(handles=[line_3, line_4])
plt.draw()

plt.pause(1000)
