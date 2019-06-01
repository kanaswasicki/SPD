
def przygotowanie_danych(nazwa):
    with open(nazwa) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    content = [int(val) for line in content for val in line.split()]
    ilosc_maszyn = content[0]
    ilosc_zadan = content[1]
    index = 4
    tabela = []
    for x in range(ilosc_maszyn):
        temp = []
        for y in range(ilosc_zadan):
            temp.append([content[index], content[index+1]])
            index +=2
        tabela.append(temp)
        index +=1
    return tabela

