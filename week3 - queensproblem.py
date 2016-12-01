import sys


def check(a, i):  # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or  # niet in dezelfde kolom
                i + n in [a[j] + j for j in range(n)] or  # niet op dezelfde diagonaal
                i - n in [a[j] - j for j in range(n)])  # niet op dezelfde diagonaal


def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("x", end=" ")
            else:
                print("*", end=" ")
        print()
    print()


def rsearch(N):
    global a, oh_lord
    for i in range(N):
        if check(a, i):
            a.append(i)
            if len(a) == N and a not in oh_lord:
                oh_lord.append(a)
                a = []
                return True  # geschikte a gevonden
            else:
                if rsearch(N):
                    return True
            del a[-1]  # verwijder laatste element
    return False


def perm(a):
    assert a
    if len(a) == 1:
        return [a]
    else:
        ap = []
        for i in range(len(a)):  # bepaal alle permutaties die
            # beginnen met a[i]
            ap2 = perm(a[:i] + a[i + 1:])  # bepaal permutaties van lijst
            # zonder a[i]
            ap += [[a[i]] + p for p in ap2]  # plaats voor iedere
            # permutatie a[i]
    return ap


def search_all_things(N):
    if rsearch(N):
        search_all_things(N)


oh_lord = []
a = []  # a geeft voor iedere rij de kolompositie aan
t = 0

sys.setrecursionlimit(10000)

search_all_things(8)
for queen in oh_lord:
    print(queen)
print(len(oh_lord))
printQueens(a)
