import re

# dict
f = open('bible.txt', 'r')

d = {}
count = 0
words = []
for l in f:
    a = re.sub("[^a-zA-Z]", " ", l).split()
    for k in a:
        k = k.lower()
        words.append(k)
        if k in d:
            d[k] = d[k] + 1
        else:
            d[k] = 1
            count += 1

f.close()

f = open('frequency-dict.txt', 'w')
f.write("FREQUENCY DICT-> WORD COUNT: " + str(count) + '\n')
for k in d:
    f.write(str(k) + ': ' + str(d[k]) + '\n')
f.close()


# trie

class Node():
    def __init__(self, e=None, n=0):
        self.element = e
        self.count = n

    def __repr__(self, n=""):
        result = ""
        if self.count > 0:
            result += n + ": " + str(self.count) + "\n"
        if self.element != None:
            for key in self.element:
                result += self.element[key].__repr__(n + key)
        return result

    def size(self):
        result = 0
        if self.count > 0:
            result += 1
        if self.element != None:
            for key in self.element:
                result += self.element[key].size()
        return result

    def insert(self, e):
        if e:
            if self.element:
                if e[0] in self.element.keys():
                    self.element[e[0]].insert(e[1:])
                else:
                    self.element[e[0]] = Node()
                    self.element[e[0]].insert(e[1:])
            else:
                self.element = {e[0]: Node()}
                self.element[e[0]].insert(e[1:])
        else:
            self.count += 1


class Trie():
    def __init__(self):
        self.root = None

    def __repr__(self):
        if self.root:
            return self.root.__repr__()

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def insert(self, e):
        if self.root:
            self.root.insert(e)
        else:
            self.root = Node()
            self.root.insert(e)


t = Trie()

for word in words:
    t.insert(word)

f = open('frequency-trie.txt', 'w')
f.write("FREQUENCY TRIE -> WORD COUNT: " + str(t.size()) + '\n')
f.write(t.__repr__())
f.close()
