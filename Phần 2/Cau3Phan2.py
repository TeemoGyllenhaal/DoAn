from sympy.plotting import plot
from sympy import symbols
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
def ham_bac_4(a,b,c,x):
    f = a*x**4+b*x**2+c
    return f
def dao_ham_bac_1():
    x = symbols('x')
    y1 = diff(ham_bac_4(1,-2,-3,x),x)
    print("Kết quả đạo hàm bậc 1: ",y1)
    return y1
def dao_ham_bac_2():
    x = symbols('x')
    y1 = diff(diff(ham_bac_4(1,-2,-3,x),x),x)
    print("Kết quả đạo hàm bậc 2: ",y1)
    return y1
def dao_ham_bac_3():
    x = symbols('x')
    y1 = diff(diff(diff(ham_bac_4(1,-2,-3,x),x),x),x)
    print("Kết quả đạo hàm bậc 3: ",y1)
    return y1
dao_ham_bac_1()
dao_ham_bac_2()
dao_ham_bac_3()

def ve_do_thi_1(a,b,c):
    x = np.linspace(-10, 10, 30)
    fig, ax = plt.subplots()
    y1 = ham_bac_4(1,-2,-3,x)
    y2 = a(x)
    y3 = b(x)
    y4 = c(x)
    ax.plot(x,y1,label = r'$y = x^{4}-2x^{2}-3$',marker=10)
    ax.plot(x,y2,label = r'$y^{1} = 4x^{3}-4x$',marker=7)
    ax.plot(x,y3,label = r'$y^{2} = 12x^{2}-4$',marker=6)
    ax.plot(x,y4,label = r'$y^{3} = 24x$',marker=1)
    ax.set_xlabel('Trục hoành x')
    ax.set_ylabel('Trục tung y')
    ax.set_title("Đồ thị phương trình y và các đạo hàm bậc 1, 2, 3")
    ax.legend()
    plt.show()
def main():
    ve_do_thi_1(lambda x: 4*x**3 - 4*x, lambda x2:12*x2**2 - 4, lambda x3: 24*x3)   
if __name__ == "__main__":
    main()

