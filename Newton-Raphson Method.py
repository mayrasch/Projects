# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 13:04:51 2026

@author: mayra
"""

# Newton-Raphson Method

import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')

f = x**4 - x - 1

f_prime = sp.diff(f, x)

print("f(x) =", f)
print("f'(x) =", f_prime)

x_n = float(input("\nEnter the initial guess of the root: "))
n = int(input("\nEnter the number of iterations wanted: "))

errors=[]
iterations = list(range(0, n))

for iteration in range(n):
    f_value = f.subs(x,x_n)
    f_prime_value = f_prime.subs(x,x_n)
    print("\nThis is iteration number:",iteration)
    print("The current approximation of the root is: x=",x_n)
    print("The value of the slope at that point is: f'(x)=",f_prime_value)
    errors.append(abs(f_value))
    x_n = x_n - (f_value/f_prime_value)
    print("The new approximation of the root is: x=",x_n)
    
print("The final approximation of the root of the function after ",n," iterations is:",x_n)

plt.plot(iterations, errors)
plt.yscale('log')
plt.xlabel('Iteration Number')
plt.ylabel('|f(c)|')
plt.title('Absolute Error vs Iteration Number (Newton-Raphson Method)')
plt.show()



