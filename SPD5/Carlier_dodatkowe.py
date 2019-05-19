def licz_b(U, pi, tabela):
    p = 0
    for i in pi:
        r = tabela[i][0]
        p = max(p, r) + tabela[i][1]
        if U == p + tabela[i][2]:
            j = i
    return j


def licz_a(U, pi, tabela, b):
    q = tabela[b][2]
    mx = pi.index(b)
    for i in pi:
        p = 0
        r = tabela[i][0]
        mi = pi.index(i)
        for a in range(mi, mx+1):
            p += tabela[pi[a]][1]
        if U == r+p+q:
            return i


def licz_c(pi, tabela, a, b):
    flaga = 0
    a = pi.index(a)
    b = pi.index(b)
    for i in range(a, b+1):
        if tabela[pi[i]][2] < tabela[pi[b]][2]:
            j = pi[i]
            flaga = 1
    if flaga == 1:
        return j
    else:
        return []


def wyznacz_L(pi, c, b, UB, rpq, tabela):
    L = []
    for i in pi[0:pi.index(c)]:
        L.append(i)
    for i in pi[pi.index(b)+1:]:
        L.append(i)
    for i in L:
        if UB - sum(rpq) >= tabela[i][1]:
            L.pop(L.index(i))
    return L


def eliminacja(L, tabela, UB, rpq, b):
    for i in L:
        if UB <= tabela[i][0] + tabela[i][1] + rpq[1] + tabela[b][2]:
            tabela[i][0] = max(tabela[i][0], rpq[0]+rpq[1])
        if UB <= rpq[0] + tabela[i][1] + rpq[1] + tabela[i][2]:
            tabela[i][2] = max(tabela[i][2], rpq[2]+rpq[1])
    return tabela
