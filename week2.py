def machtv3(a, n):
    assert n > 0
    x = 0
    m = 1
    while n > 0:
        if n % 2 == 0:
            a *= a
            x += 1
            n /= 2
        else:
            m *= a
            n -= 1
            x += 1
    return m, x


class mystack(list):
    stack = []

    def __repr__(self):
        return "Size: " + str(len(self.stack)) + "\nStack: " + str(self.stack)

    def __init__(self, initialStack=[]):
        self.stack = initialStack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            temp = self.stack[-1]
            self.stack = self.stack[:-1]
            return temp
        else:
            return None

    def peek(self, index):
        assert index >= 0
        assert index < len(self.stack)
        return self.stack[index]

    def isEmpty(self):
        return len(self.stack) == 0


def valid_expression(string):
    stack = []
    for c in string:
        assert c in "<>[]()" and len(string) > 1

    for c in string:
        if c in "<[(":
            stack.append(c)
        else:
            if c == '>' and stack.pop() != '<':
                return False
            elif c == ']' and stack.pop() != '[':
                return False
            elif c == ')' and stack.pop() != '(':
                return False
    return len(stack) == 0


def binbin(number):
    n = ''
    return ['' if n == 0 else number(n / 2) + str(n % 2)]


def binbin(n):
    assert n >= 0, "cannot convert negative number to binary"
    if n == 0:
        return '0'
    s = ""
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    return '0b' + s


print(machtv3(2, 1000)[1])

stack = mystack()

stack.push("1")
stack.push("2")
stack.push("3")
stack.push("4")
print(stack)
stack.pop()
stack.pop()
print(stack)
print(stack.peek(1))

print(valid_expression("((<>))"))  # true
print(valid_expression("((<()>))"))  # true
print(valid_expression("((<()>))((<()>))((<()>))((<()>))((<()>))((<()>))"))  # true
print(valid_expression("[][][][]<><>(([()]))"))  # true
print(valid_expression("([)]"))  # false
print(valid_expression("(("))  # false
print(valid_expression("(()"))  # false

print(binbin(100) == '0b1100100')
print(binbin(2) == '0b10')
print(binbin(32) == '0b100000')
print(binbin(5) == '0b101')
