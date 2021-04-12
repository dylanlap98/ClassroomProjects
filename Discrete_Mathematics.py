
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


print(permutations_calc(6,1))


