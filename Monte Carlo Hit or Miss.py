# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:06:27 2026

@author: mayra
"""

import random
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

print("Lets compute the integral of f(x) over the interval [a,b] using the Monte Carlo Hit or Miss method")

x=sp.symbols('x')
f_expr = sp.sympify(input("\nEnter the function f(x) = "))
f = sp.lambdify(x, f_expr, "math")

a = int(input("\nEnter a: "))
b = int(input("Enter b: "))
print("\nYou want to integrate f(x)=",f_expr," from ",a," to ",b)
n = int(input("\nEnter n: "))

f_max=max(f(x) for x in range (a+1,b+1))
f_min=min(f(x) for x in range (a+1,b+1))
A_rectangle=(b-a)*(f_max-f_min)

print("\nThe maximum value is: f(x)=",f_max)
print("\nThe minimum value is: f(x)=",f_min)
print("\nThe area of the rectangle is A=",A_rectangle)

y_random=[random.uniform(f_min,f_max) for _ in range(n)]
x_random=[random.uniform(a,b) for _ in range(n)]
zipped_pairs = zip(x_random,y_random)
xy_pairs = list(zipped_pairs)
print("\nThe random points are: (x,y)=",xy_pairs)

n_below = 0
x_above = []
y_above = []
x_below = []
y_below = []
for x_value, y_value in xy_pairs:
    print("\nThe point being evaluated is (",x_value,",",y_value,")")
    f_value=f(x_value)
    print("f(x)=",f_value)
    if y_value < f_value:
        n_below += 1
        x_below.append(x_value)
        y_below.append(y_value)
        print("This point is under f(x)")
    else:
        x_above.append(x_value)
        y_above.append(y_value)

print("\nNumber of points below f(x):", n_below)
    
A=A_rectangle*(n_below/n)
print("\nThe approximate integral is of f(x) over [a,b] is: ",A)

x_f = np.linspace(a, b, 400)
y_f = f(x_f)

plt.scatter(x_above,y_above,c='red',alpha=0.3)
plt.scatter(x_below,y_below,c='green',alpha=0.3)
plt.plot(x_f,y_f)
plt.xlabel("x")
plt.ylabel("y")
plt.show()




