# -*- coding: utf-8 -*-

# Bisection Method

import sympy as sp
import random
import matplotlib.pyplot as plt

x=sp.symbols('x')

f = x**4 - x - 1

a = float(input("\nEnter the initial guess of the root: "))
b = 3

fa=f.subs(x,a)
fb=f.subs(x,b)

while fa * fb > 0:
    b=random.random()
    fb=f.subs(x,b)

errors=[]

n = int(input("\nEnter the number of iterations wanted: "))

iterations = list(range(0, n))

for iteration in range (n):
    
    print("\nThis is iteration number",iteration)
    print("The interval is=[", a, ",", b, "]")
    
    c=(a+b)/2
    fc=f.subs(x,c)
    
    print("c =", c)
    print("f(c) =", fc)
    
    if (fa*fc)<0:
        print("f(c) and f(a) have opposite signs so the upper bound (a) is replaced by c")
        b=c
        
    elif (fb*fc)<0:
        print("f(c) and f(b) have opposite signs so the lower bound (b) is replaced by c")
        a=c
        
    else:
        print ("The root is:",c)
    
    errors.append(abs(fc))

print("\nThe approximate root is",c)

plt.plot(iterations, errors)
plt.yscale('log')
plt.xlabel('Iteration Number')
plt.ylabel('|f(c)|')
plt.title('Absolute Error vs Iteration Number (Bisection Method)')
plt.show()




