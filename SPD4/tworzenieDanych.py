import random


def tworzenie_danych(zadania, maszyny):
    tekst = str(zadania) + "\t" + str(maszyny) + "\n"
    for i in range(0, zadania):
        for j in range(0, maszyny):
            tekst += str(random.randrange(0, 100, 1)) + "\t"
        tekst += "\n"
    return tekst


for a in range(1, 4):
    for i in range(10, 501):
        tekst = tworzenie_danych(i, 3)
        open("data" + str(a) + "\\" + str(i) + "data.txt", "w").write(tekst)
