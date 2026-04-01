# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:27:26 2026

@author: mayra
"""

import random
import sympy as sp

print("Lets compute the integral of f(x) over the interval [a,b] using the Monte Carlo method")

x = sp.symbols('x')
f = sp.sympify(input("\nEnter f(x) = "))

a = float(input("\nEnter a: "))
b = float(input("\nEnter b: "))
w = b - a

n = int(input("\nEnter n (number of random sample points): "))
n_values = [random.uniform(a, b) for _ in range(n)]

total = 0
for val in n_values:
    f_value = f.subs(x, val)
    total += f_value

average=total/n
A=w*average

print("The integral of f(x) over the interval [a,b] is approximately A =", A)