import sys


class Entry:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.next = None

    def __repr__(self):
        return "Key: " + str(self.key) + "\n Value: " + str(self.value) + (
            "\t" + self.next.__repr__() if self.next is not None else "")


class Table:
    def __init__(self, length):
        self.used = 0
        self.len = length
        self.table = [None] * length

    def __repr__(self):
        for i in self.table:
            print(i)

    def insert(self, e):
        hash = (e.key % self.len)
        if self.table[hash] is None:
            self.table[hash] = e
            self.used += 1
            if self.used > 0.75 * self.len:
                self.rehash(self.len * 2)
        else:
            entry = self.table[hash]
            while entry.next is not None and entry.key != e.key:
                entry = entry.next
            if entry.key == e.key:
                entry.value = e.value
            else:
                entry.next = e

    def search(self, key):
        hash = (key % self.len)
        if self.table[hash] is not None:
            entry = self.table[hash]
            while entry is not None and entry.key != key:
                entry = entry.next
            if entry is None:
                return -1
            else:
                return entry
        else:
            return -1

    def delete(self, key):
        hash = (key % self.len)
        if self.table[hash] is None:
            return -1
        else:
            entry = self.table[hash]
            prev = None
            while entry.next is not None and entry.key != key:
                prev = entry
                entry = entry.next
            if entry.key == key:
                if prev is None:
                    self.table[hash] = entry.next
                else:
                    prev.next = entry.next

    def rehash(self, new_len):
        print("REHASHING NEW LENGTH ", new_len)
        if new_len > self.len:
            oldlen = self.len
            oldTable = self.table
            self.table = [None] * new_len
            self.used = 0
            self.len = new_len

            for i in range(oldlen):
                if oldTable[i] is not None:
                    self.insert(oldTable[i])
            for i in self.table:
                if i is not None:
                    print(i)


import random

sys.setrecursionlimit(100000000)
t = Table(1)

print("INSERTING")

for i in range(200):
    t.insert(Entry(i, random.uniform(0, 1000)))

for i in range(100):
    t.delete(i)

print("DELETED")
for i in t.table:
    if i is not None:
        print(i)

import random

hashdict = dict()
while (True):
    r = random.random()
    if r not in hashdict.values():
        hr = hash(r) % (2 ** 32)
        if hr in hashdict.keys():
            print(repr(r) + ", " + repr(hashdict[hr]) + ": " + repr(hr))
            break
        hashdict[hr] = r

def B(n, k):
    C = [0 for i in range(k + 1)]
    C[0] = 1  # since nC0 is 1

    for i in range(1, n + 1):
        j = min(i, k)
        while j > 0:
            C[j] = C[j] + C[j - 1]
            j -= 1

    return C[k]


print((B(100, 50)))


def f(n):
    assert type(n) == int
    assert n <= 1000
    coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    ways = [1] + ([0] * n)
    for coin in coins:
        for i in range(coin, n + 1):
            ways[i] += ways[i - coin]
    return ways[n]

print(f(100))

