import math
import random


def mymax(a):
    assert len(a) > 0
    assert len([element for element in a if type(element) != int and type(element) != float]) == 0

    highest = a[0]
    for element in a:
        if element > highest:
            highest = element
    return highest

def getNumbers(s):
    result = []
    check = False
    counter = -1
    for c in s:
        if c >= "0" and c <= "9":
            if not check:
                counter += 1
                result.append(c)
            else:
                result[counter] += c
            check = True
        else:
            check = False
    return result

def myprime(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
    return a

def birthdayParty():
    odds = []
    for i in range(100):
        temp = []
        for j in range(23):
            temp.append(random.randint(1, 365))
            if len(temp) != len(set(temp)):
                odds.append(len(temp))
                break
    return len(odds)/100



print(mymax([1, 2, 2, 3, 4, 5]))
print(getNumbers("een123zin45 6met-632meerdere+7777getallen"))
print(birthdayParty())
for x in myprime(1000):
    print(x, end=" ")
