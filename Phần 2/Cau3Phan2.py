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
    return y1
def dao_ham_bac_2():
    x = symbols('x')
    y1 = diff(diff(ham_bac_4(1,-2,-3,x),x),x)
    return y1
def dao_ham_bac_3():
    x = symbols('x')
    y1 = diff(diff(diff(ham_bac_4(1,-2,-3,x),x),x),x)
    return y1

def ve_do_thi_cach_1():
    x = symbols('x')
    y1 = plot(
        ham_bac_4(1,-2,-3,x), 
        diff(ham_bac_4(1,-2,-3,x),x), 
        diff(diff(ham_bac_4(1,-2,-3,x),x),x), 
        diff(diff(diff(ham_bac_4(1,-2,-3,x),x),x),x),
        (x, -10, 10), title = "Đồ Thị y và đạo hàm các bậc của nó", ylabel = "Trục tung", xlabel = "Trục hoành",legend = True)
    return y1


def ve_do_thi_1(a,b,c):
    x = np.linspace(-10, 10, 100)
    fig, ax = plt.subplots()
    y1 = ham_bac_4(1,-2,-3,x)
    y2 = a(x)
    y3 = b(x)
    y4 = c(x)
    ax.plot(x,y1,label = dao_ham_bac_1(),linestyle='--')
    ax.plot(x,y2,label = "hj",linestyle='dashdot')
    ax.plot(x,y3,label = "hjg",linestyle=(0, (3, 1, 1, 1)))
    ax.plot(x,y4,label = "hjf",linestyle=(0, (3, 10, 1, 10, 1, 10)))
    ax.set_xlabel('Trục hoành x')
    ax.set_ylabel('Trục tung y')
    ax.set_title("Đồ thị phương trình y và đạo hàm")
    ax.legend()
    plt.show()
def main():
    
    #ve_do_thi()
    #dao_ham_bac_2()
    #dao_ham_bac_3()
    #ve_do_thi_1(lambda x: 4*x**3 - 4*x, lambda x2:12*x2**2 - 4, lambda x3: 24*x3)
    ve_do_thi_cach_1()
    
if __name__ == "__main__":
    main()

