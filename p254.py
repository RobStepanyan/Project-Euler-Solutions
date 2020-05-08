import math

class Euler254:
    def __init__(self):
        self.q = input()
        self.n = []
        self.m = []
        self.results = {}
        for _ in range(int(self.q)):
            line = input().split()
            self.n.append(int(line[0]))
            self.m.append(int(line[1]))
        self.__class__.calc(self)

    @classmethod
    def f(cls, num):
        """
        The sum of the factorials of the digits
        """
        return sum((math.factorial(int(digit)) for digit in str(num)))
    
    @classmethod
    def sf(cls, num):
        """
        The sum of the digits of f()
        """
        return sum((int(digit) for digit in str(cls.f(num))))

    @classmethod
    def g(cls, int_):
        """
        The smallest positive integer such that sf(num) = int_
        """
        num = 1
        while cls.sf(num) != int_:
            num += 1
        return num - 1

    @classmethod
    def sg(cls, int_):
        """
        The sum of the digits of g(i)
        """
        return sum((int(digit) for digit in str(cls.g(int_))))

    def calc(self):
        for n, m in zip(self.n, self.m):
            s = 0
            for i in range(1, n+1):
                if i in self.results:
                    s += self.results[i]
                else:
                    res = self.__class__.sg(i)
                    self.results[i] = res
                    s += res
            print(s)

Euler254()
