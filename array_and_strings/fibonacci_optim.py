"""this program is an optimum way to commute n fibonacci terms O(n).. In this we just compute the fibonacci of a 
number once and then compute others only by adding the elements from the stores numbers thus taking only constant time 
every time using Memoization with function decorators"""

from __future__ import print_function # this is to use the end param in print to print all numbers in one line

class Memoize: #Memoization with class decorators
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
	    self.memo[args] = self.fn(*args)
        return self.memo[args]

def memoize(f):    #Memoization with function decorators
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize     #this is a decorator added to store the already computed values
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def main():
    n = input('Enter a number: ')
    for i in range(0,n):
        print (fib(i), end=' ')
    print ('\n')

if __name__ == "__main__":
    main()