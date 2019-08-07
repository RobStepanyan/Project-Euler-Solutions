"""
Amicable numbers

Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def p021():
    def proper_divisors(num):
        divisors = [1]
        for i in range(2, int(num)//2+1):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors)

    def amicable(num):
        x = proper_divisors(num)
        if x == num or x > num:
            return False
        if proper_divisors(x) == num:
            return x + num
        return False

    sum_of_pairs = 0
    for num in range(1, 10000):
        if amicable(num) != False:
            sum_of_pairs += amicable(num)

    print('p021: ', sum_of_pairs)


"""
Names scores

Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
# Getting the list of names from the .txt file


def p022():
    file = open('Problems 1-50\p022_names.txt', 'r')
    s = str(list(file)[0])
    file.close()
    l = sorted([item[1:-1] for item in s.split(',')])

    alphabet = sorted(['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A',
                       'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M'])

    def worth(s):
        worth = 0
        for symbol in s:
            worth += alphabet.index(symbol) + 1
        return worth

    s = 0
    for name in l:
        s += (l.index(name)+1) * worth(name)

    print('p022: ', s)


"""
Non-abundant sums

Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


def p023():
    def proper_divisors(num):
        divisors = [1]
        for i in range(2, int(num)//2+1):
            if num % i == 0:
                divisors.append(i)
        return sum(divisors)

    abundants = []
    for i in range(11, 28123):
        if proper_divisors(i) > i:
            abundants.append(i)

    possible_sums = set()
    for x1 in abundants:
        for x2 in abundants:
            possible_sums.add(x1+x2)
    possible_sums = tuple(possible_sums)

    s = 0
    for i in range(1, 28124):
        if i not in possible_sums:
            s += i

    print('p023: ', s)


"""
Lexicographic permutations

Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Found on youtube:
Step1: Find the laregest i so s[i-1] < s[i]
Step2: Find j so s[i-1] < s[j]
Step3: Swap s[i-1] and s[j]
Step4: Reverse the order of characters s[i:]
"""


def p024(n=1000000):
    s = ' 0123456789'

    def find_i(s):
        for i in range(len(s)-1, 0, -1):
            if s[i-1] < s[i]:
                return i

    def find_j(s):
        i = find_i(s)-1
        for j in range(len(s)-1, i-1, -1):
            if s[i] < s[j]:
                return j

    def swap(s, i, j):
        return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

    def reverse_from_i(s, i):
        from_i = s[i:]
        return s[:i] + from_i[::-1]

    permutation_no = 1
    while permutation_no < n:
        i = find_i(s)
        j = find_j(s)
        s = swap(s, i-1, j)
        s = reverse_from_i(s, i)
        permutation_no += 1

    print('p024: ', s)


"""
1000-digit Fibonacci number

Problem 25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def p025(n=1000):
    x1, x2 = 1, 0
    x3 = x1 + x2

    q = 1
    while len(str(x3)) != n:
        x1, x2 = x2, x3
        x3 = x1 + x2
        q += 1

    print('p025: ', q)


p021()
# p021:  31626
p022()
# p022:  871198282
p023()
# p023:  4179871
p024()
# p024:   2783915460
p025()
# p025:  4782