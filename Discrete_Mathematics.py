import math


# function to solve permutations of 'n' elements (Chapter 9.2)
def permutations_calc(n, r):
    n_temp = n
    r_temp = n - r
    numerator = 1
    denominator = 1
    while n_temp > 1:
        numerator = numerator * n_temp
        n_temp -= 1
    while r_temp > 1:
        denominator = denominator * r_temp
        r_temp -= 1
    #print(numerator, denominator)
    return numerator/denominator


print(permutations_calc(9,3))


def r_combinations(n, r):
    numerator = permutations_calc(n, r)
    denominator = math.factorial(r)
    return numerator / denominator

# question may be formulated as: 7 choose 5?
#print(r_combinations(7, 5))
print(r_combinations(9, 3))


# Assuming that all years have 365 days and all birthdays occur with equal probability, how large must n be so that
# in any randomly chosen group of n people, the probability that two or more have the same birthday is at least
# 'target'?
def birthday_problem(target):
    n = 1
    sub = 1
    for i in range(364, 0, -1):
        n = 365 - i
        #print('this is n', n)
        #print(i)
        sub = sub * (i + 1)
        r = 365 ** n
        calc = (r - sub) / r
        if calc >= target:
            break
    print(n)


#print(birthday_problem(.5))


