from sympy.plotting import plot
from sympy import symbols
from sympy import *
import numpy as np
def ham_bac_4(a,b,c,x):
    f = a*x**4+b*x**2+c
    return f

def dao_ham_bac_1():
    x = symbols('x')
    y1 = diff(ham_bac_4(1,-2,-3,x),x)
    return y1

def dao_ham_bac_2():
    x = symbols('x')
    y1 = diff(diff(ham_bac_4(1,-2,-3,x),x),x)
    return y1

def dao_ham_bac_3():
    x = symbols('x')
    y1 = diff(diff(diff(ham_bac_4(1,-2,-3,x),x),x),x)
    return y1


def ve_do_thi():
    x = symbols('x')
    y1 = plot(
        ham_bac_4(1,-2,-3,x), 
        diff(ham_bac_4(1,-2,-3,x),x), 
        diff(diff(ham_bac_4(1,-2,-3,x),x),x), 
        diff(diff(diff(ham_bac_4(1,-2,-3,x),x),x),x),
        (x, -10, 10), title = "Đồ Thị y và đạo hàm các bậc của nó", ylabel = "Trục tung", xlabel = "Trục hoành")    
    return y1

def ve_do_thi_cach_2():
    x = symbols('x')
    y  = plot((ham_bac_4,dao_ham_bac_1,dao_ham_bac_2,dao_ham_bac_3),(x,-10,10),
            title = "Đồ Thị y và đạo hàm các bậc của nó", ylabel = "Trục tung", xlabel = "Trục hoành")
    return y
def main():
    ve_do_thi()
if __name__ == "__main__":
    main()

