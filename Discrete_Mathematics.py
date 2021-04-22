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


#print(permutations_calc(9,3))


def r_combinations(n, r):
    numerator = permutations_calc(n, r)
    denominator = math.factorial(r)
    return numerator / denominator

# question may be formulated as: 7 choose 5?
print(r_combinations(4, 1))
#print(r_combinations(9, 3))
#print(r_combinations(10, 3))
#print(r_combinations(11, 5))

#print(r_combinations(5,3) * r_combinations(7,2))
print(r_combinations(12,5) - r_combinations(7,5))
#print(r_combinations(13, 6) - r_combinations(10, 3) - r_combinations(11, 4) - r_combinations(11, 4))


# Prime Number Calculator
def is_prime(num):
    # If given number > 1
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num / 2) + 1):
            # If num is divisible by any number between
            # 2 and n / 2, it's not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")


# is_prime(11)

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


