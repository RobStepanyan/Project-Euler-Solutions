"""
Multiples of 3 and 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def p001():
    s = 0
    for num in range(1, 1000):
        if num % 3 == 0 or num % 5 == 0:
            s += num
    print('p001: ', s)


"""
Even Fibonacci numbers

Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def p002():
    f1, f2, f3, s = 1, 1, 1, 0
    while f3 < 4000000:
        if f3 % 2 == 0:
            s += f3
        f1, f2 = f2, f3
        f3 = f1 + f2
    print('p002: ', s)


"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def p003(num=600851475143):
    def prime(num):
        for d in range(2, int(num) // 2+1):
            if num % d == 0:
                return False
        return True

    def all_prime(lst):
        for item in lst:
            if not prime(item):
                return False
        return True

    def find_two_branches(n):
        for x1 in range(2, int(n)):
            if n % x1 == 0:
                x2 = n / x1
                break
        return x1, x2

    if prime(num):
        print('p003: ', num)
    else:
        b1, b2 = find_two_branches(num)
        p_factors = [b1, b2]
        while not all_prime(p_factors):
            for item in p_factors:
                if not prime(item):
                    del p_factors[p_factors.index(item)]
                    b1, b2 = find_two_branches(item)
                    p_factors.extend([b1, b2])
        print('p003: ', int(max(p_factors)))


"""
Largest palindrome product

Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def p004():
    def palindrome(num):
        if str(num) == str(num)[::-1]:
            return True
        return False
    palindromes = []
    for n1 in range(100, 1000):
        for n2 in range(100, 1000):
            if palindrome(n1*n2):
                palindromes.append(n1*n2)
    print('p004: ', max(palindromes))


"""
Smallest multiple

Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def p005():
    num = 20
    while True:
        divisible = True
        for d in range(1, 21):
            if not num % d == 0:
                divisible = False
        if divisible == True:
            break
        else:
            num += 2520
    print('p005: ', num)


p001()
# p001:  233168
p002()
# p002:  4613732
p003()
# p003:  6857
p004()
# p004:  906609
p005()
# p005:  232792560
