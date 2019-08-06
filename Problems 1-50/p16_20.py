"""
Power digit sum

Problem 16
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def p016():
    number = str(2**1000)
    list_of_digits = [int(digit) for digit in number]
    print('p016: ', sum(list_of_digits))


"""
Number letter counts

Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""


def p017():
    def name_a_number(num):
        list_of_digits = ['one', 'two', 'three', 'four',
                          'five', 'six', 'seven', 'eight', 'nine']
        if len(str(num)) == 1:
            return list_of_digits[num-1]
        else:
            if len(str(num)) == 2:
                if num < 20:
                    list_of_names = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                                     'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
                    return list_of_names[num-10]
                else:
                    first_part = ['twenty', 'thirty', 'forty',
                                  'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
                    last_part = ['', 'one', 'two', 'three', 'four',
                                 'five', 'six', 'seven', 'eight', 'nine', 'ten']
                    return first_part[int(str(num)[0])-2] + last_part[int(str(num)[1])]
            elif num == 1000:
                return 'onethousand'
            else:
                if str(num)[-1] == '0' and str(num)[-2] == '0':
                    return list_of_digits[int(str(num)[0])-1] + 'hundred'
                elif str(num)[1] == '0':
                    return list_of_digits[int(str(num)[0])-1] + 'hundredand' + list_of_digits[int(str(num)[2])-1]
                elif int(str(num)[-2:]) < 20:
                    list_of_names = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                                     'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
                    return list_of_digits[int(str(num)[0])-1] + 'hundredand' + list_of_names[int(str(num)[-2:])-10]
                else:
                    first_part = ['', 'twenty', 'thirty', 'forty',
                                  'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
                    last_part = ['', 'one', 'two', 'three', 'four',
                                 'five', 'six', 'seven', 'eight', 'nine', 'ten']
                    return list_of_digits[int(str(num)[0])-1] + 'hundredand' + first_part[int(str(num)[-2])-1]+last_part[int(str(num)[-1])]

    s = 0
    for num in range(1, 1001):
        s += len(name_a_number(num))

    print('p017: ', s)


"""
Maximum path sum I

Problem 18
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""
triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]


def p018():
    # Not solved by me
    for x in range(len(triangle)-1, -1, -1):
        for y in range(0, x):
            triangle[x-1][y] += max(triangle[x][y], triangle[x][y+1])
    print('p018: ', triangle[0][0])


"""
Counting Sundays

Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""


def p019():
    def leap_year(year):
        if year % 400 == 0 or year % 4 != 0:
            return False
        return True

    MONTH = {
        'January': 31, 'February': 28, 'March': 31,
        'April': 30, 'May': 31, 'June': 30, 'July': 31,
        'August': 31, 'September': 30, 'October': 31,
        'November': 30, 'December': 31
    }

    WEEK_DAY = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']

    day = 1
    month = 'January'
    year = 1901
    week_day = 'Monday'

    count = 0
    while not (year == 2000 and month == 'December' and day == 31):
        # Check if the first day of the month is Monday
        if day == 1 and week_day == 'Monday':
            count += 1

        # Change the day, month and year if needed
        day += 1
        if day > MONTH[month]:
            day = 1
            current_month_index = list(MONTH.keys()).index(month)
            month_keys = list(MONTH.keys())
            if current_month_index == 11:
                month = month_keys[0]
            else:
                month = month_keys[current_month_index + 1]

            if month == 'January':
                year += 1
                if leap_year(year):
                    MONTH['February'] = 29
                else:
                    MONTH['February'] = 28

        # Change the weekday
        current_weekday_index = WEEK_DAY.index(week_day)
        if current_weekday_index == 6:
            week_day = WEEK_DAY[0]
        else:
            week_day = WEEK_DAY[current_weekday_index + 1]

    print('p019: ', count-1)


"""
Factorial digit sum

Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100vvvv
"""


def p020(num=100):
    def factorial(num):
        prd = 1
        for i in range(2, num+1):
            prd *= i
        return prd

    ans = sum([int(digit) for digit in str(factorial(num))])
    print('p020: ', ans)

p016()
# p016:  1366
p017()
# p017:  21124
p018()
# p018:  1074
p019()
# p019:  171
p020()
# p020:  648