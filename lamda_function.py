from functools import reduce
n = 5
f = lambda n : reduce(lambda x,y : x*y , range(1,n+1))
print("Factorial of ",n,"is: ",f(n))
