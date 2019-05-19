def licz_b(U, n, tabela):
    p = 0
    for i in n:
        r = tabela[i][0]
        p = max(p, r) + tabela[i][1]
        if U == p + tabela[i][2]:
            j = i
    return j


def licz_a(U, n, tabela, b):
    q = tabela[b][2]
    mx = n.index(b)
    for i in n:
        p = 0
        r = tabela[i][0]
        mi = n.index(i)
        for a in range(mi, mx+1):
            p += tabela[n[a]][1]
        if U == r+p+q:
            return i


def licz_c(n, tabela, a, b):
    flaga = 0
    a = n.index(a)
    b = n.index(b)
    for i in range(a, b+1):
        if tabela[n[i]][2] < tabela[n[b]][2]:
            j = n[i]
            flaga = 1
    if flaga == 1:
        return j
    else:
        return []

