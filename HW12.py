import numpy as np


# Homework 12 Python

# 1. using numpy to generate 28 integers that are all from 1-100.
print('\n', 'Question 1:')
a = np.random.randint(0, 101, 28)
print(a)

# 2. reshape these 28 integers into a 2-D array of 4 x 7, stored in variable A, display A properly
print('\n', 'Question 2:')
a = np.reshape(a, [4, 7])
print(a)

# 3. Compute the sum, mean, and standard deviation of A (all integers), display them properly
print('\n', 'Question 3:')
print('sum:', np.sum(a))
print('mean:', np.mean(a))
print('std:', np.std(a))

# 4. Compute the sum, mean, and standard deviation of each row for A, display them properly
print('\n', 'Question 4:')
print('sum:', np.sum(a, axis=1))
print('mean:', np.mean(a, axis=1))
print('std:', np.std(a, axis=1))

# 5. Display the transpose of A, and then compute the dot product matrix of A.T and A, display it
print('\n', 'Question 5:')
print(a)
AT = np.transpose(a)
print(AT)
print('product of a:', np.prod(a, axis=0))
print('product of AT:', np.prod(AT, axis=0))


# 6. Sort A's each column, display it properly.
print('\n', 'Question 6:')
print('sort by col: \n', np.sort(a, axis=0))

# 7. Sort A's each row, display it properly
print('\n', 'Question 7:')
print('sort by row: \n', np.sort(a, axis=1))

# 8. Make B to be a revised A such that any numbers <20 in A are removed. A should not be changed. Display B properly
print('\n', 'Question 8:')
b = a[:]
b = b[(b >= 20)]
print(b)

# 9. Make C to be a revised A such that any numbers <20 in A are replaced with 0. A should not be changed. Display C
# properly. (note, there are several ways to do, please use the most efficient ways)
print('\n', 'Question 9:')
c = a[:]  # deep copy into c
#print(b)
c[(c < 20)] = 0  # rm nums less than 20 in b
print(c)

# 10. Revise A such that any numbers between 40 and 60 inclusively are replaced by 1. A is changed. Display A properly.
print('\n', 'Question 10:')
a = a[(a > 40) & (a < 60)]
print(a)
