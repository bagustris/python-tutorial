# demo tuples in python
# Tuple is similar to list
# but can be used as key in dict

# create dictionary with tuple key
d = {(x, x + 1): x for x in range(10)}

# create tuple
t = (5, 6)

# print type of tuple
print(type(t))

# print "5": key only
print(d[t])

# print "1"
print(d[(1, 2)])

/bin/bash: q: command not found
print(d[(3, 6)])
