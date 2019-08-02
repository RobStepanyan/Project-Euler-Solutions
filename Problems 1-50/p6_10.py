"""
Sum square difference

Problem 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
"""


def p006():
    sum_of_sqr = sum(list(map(lambda x: x*x, range(1, 101))))
    sqr_of_sum = sum(range(1, 101))**2
    print('p006: ', sqr_of_sum - sum_of_sqr)


"""
10001st prime

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def p007(n=10001):
    def prime(num):
        for d in range(2, int(num) // 2+1):
            if num % d == 0:
                return False
        return True
    num = 2
    prime_no = 0
    while prime_no < n:
        if prime(num):
            prime_no += 1
        num += 1
    print('p007: ', num - 1)


"""
Largest product in a series

Problem 8
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""
thousand_digits = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
""".replace("\n", "")


def p008():
    def prod(lst):
        prd = 1
        for item in lst:
            prd *= item
        return prd

    combinations = []
    for i in range(1001-13):
        lst = [int(item) for item in thousand_digits[i:i+13]]
        combinations.append(prod(lst))

    print('p008: ', max(combinations))

"""
Special Pythagorean triplet

Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
def p009():
    sum_abc = 1000
    for a in range(1, 500):
        for b in range(a, 501):
            c = sum_abc-a-b
            if a*a + b*b == c*c:
                break
        else:
            # Continue if the inner loop wasn't broken.
            continue
        # Inner loop was broken, break the outer.
        break

    print('p009: ', a*b*c)

"""
Summation of primes

Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from math import sqrt
def p010():
    def prime(num):
        for d in range(2, num//2+1):
            if num % d == 0:
                return False
        return True
    sum_of_primes = 2
    num = 3
    while num <= 2000000:
        if prime(num):
            sum_of_primes += num
        num +=2
    print(sum_of_primes)

p006()
# p006:  25164150
p007()
# p007:  104743
p008()
# p008:  23514624000
p009()
# p009:  31875000
p010()
# p010:  142913828922
