from functools import reduce
lis = [2,4,6,7,8,9]

s = (reduce(lambda x,y: x+y, lis))
print(s)
