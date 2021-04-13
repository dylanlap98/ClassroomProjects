import numpy as np

# normal array
a  = [i for i in range(10)]

# numpy array
b = np.array(range(10))

print(a)
print(b)

# 2D array
a = np.empty([4,7], dtype= int)
# print(a)  # This will print a number very small in place of 0

a = np.ones([4,7])
print(a)

# 'a range' function:
c = np.arange(4,13,2)
print(c)

# Viewing and accessing our c array that we created
print(c[0])
print(c[-1])

print('\n', '-----------------', '\n')

# 2D array
a = np.ones([4,6], dtype=int)
print(a)

# Generate normal 1d array then change this to 2d array.
a = [(i+1)*2 for i in range(20)]
print(a)
a = np.reshape(a, [4, 5])
print(a)

print(a[0,2])  # ... or ....
print(a[0][2])
print(a[1])  # get a whole row


# Deep copy
a = [i for i in range(20)]
a = np.reshape(a, [4, 5])

b = a.tolist()
print(b)

b = np.reshape(b, [4, 5])
print(b)
# go through b and when < 10 make 0
b[b<10] = 0
print(b)
# another example
b[(b < 10) | (b > 15)] = 1
print(b)

print('\n', '-----------------', '\n')

# repetition in regular python
c = [0] * 10
c = c * 2
print(c)

c = [i for i in range(10)]
c = np.array(c)
print(c)

d = c * 2
print(d)

print('\n', '-----------------', '\n')

print(a)
print(sum(a))
print(np.sum(a))

print('\n', '-----------------', '\n')

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
a = np.reshape(a, [4, 5])
b = a > 5
print(b)

print(a)
a[(a > 5) & (a < 10)] = 100  # used to replace values between these to 100
print(a)

print('\n', '-----------------', '\n')

a = np.array([[6,34,1,6], [0,5,2,-1]])
print('default a: \n', a)
print('default sort: \n', np.sort(a))  # this will not sort in place unless you "a = statement.."
print('sort axis = 0: \n', np.sort(a, axis=0))
print('sort axis = 1: \n', np.sort(a, axis=1))

print('\n', '-----------------', '\n')

a = ([6, 39,  3,  5])
print(a)
print(np.sum(a))

a = np.array([[6, 34, 1, 6], [0, 5, 2, -1]])
a[1, 0] = 1
print(a)
print(np.prod(a))

print(np.prod(a, axis=1))  # axis 1 = multiply by row, axis 0 by col

# see how numpy uses diff for subtraction in 2d array.
print(np.diff(a))

print(np.diff(a, axis=0))

print('\n', '-----------------', '\n')

# Section on standard division.
print(np.std(a))  # Using a from before ^
print(np.std(a, axis=1))  # by row
print(np.std(a, axis=0))  # by column

print(a)
print(np.min(a))
print(np.min(a, axis=1))
print(np.min(a, axis=0))

