# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 13:03:52 2026

@author: mayra
"""

import sympy as sp

print("Let's approximate the integral")

x = sp.symbols('x')
f = sp.sympify(input("Enter the function f(x) = "))
h = float(input("Enter the step size h = "))
x_value = float(input("Enter the x value where you want to approximate the derivative x = "))

df = sp.diff(f, x)

df_value = df.subs(x, x_value)
f_x_value=f.subs(x,x_value)

print("\nf(x) =", f)
print("f'(x) =", df)
print("Exact analytical derivative: f'(", x_value, ") =", df_value)

xh_fwd=x_value+h
f_xh_value_fwd=f.subs(x,xh_fwd)
df_fwd=(f_xh_value_fwd-f_x_value)/h
error_fwd=float(abs(100*(df_value-df_fwd)/df_value))
print("\nBackward difference: f'(x) =", df_fwd)
print("Percentage error=",error_fwd)

xh_bwd=x_value-h
f_xh_value_bwd=f.subs(x,xh_bwd)
df_bwd=(f_x_value-f_xh_value_bwd)/h
error_bwd=float(abs(100*(df_value-df_bwd)/df_value))
print("\nForward difference: f'(x) =", df_bwd)
print("Percentage error=",error_bwd)

df_ctr=(f_xh_value_fwd-f_xh_value_bwd)/(2*h)
error_ctr=float(abs(100*(df_value-df_ctr)/df_value))
print("\nCentral difference: f'(x) =", df_ctr)
print("Percentage error=",error_ctr)

    
    
    
    
    



