from sympy import symbols, Eq, solve
from sympy import *
def giai_he_phuong_trinh():
    x, y, z = symbols('x y z')
    eq1 = Eq(2*x - 5 * y + z, -5)
    eq2 = Eq(4*x + 2*y - 2*z, 2)
    eq3 = Eq(x + y - z, 0)
    answer = solve((eq1, eq2, eq3), (x,y,z))
    return answer

def tinh_gioi_han():
    x = symbols('x')
    f = (((x**3-3*x**2)**1/3)+((x**2-2*x)**1/2))
    answer = limit(f,x,oo)
    return answer

def tinh_dao_ham():
    x = symbols('x')
    f = (2*x-1)/(x+2)
    answer = diff(f, x)
    return answer

def tinh_nguyen_ham():
    x = symbols('x')
    f = ((x)/(x**2+1))
    answer = integrate(f,x)
    return answer

def tinh_tich_phan():
    x = symbols('x')
    f = (1-x*tan(x))/(x**2*cos(x)+x)
    answer = integrate(f, (x,(2*pi/3),pi))
    return answer
def main():
    a = giai_he_phuong_trinh()
    print ("Kết quả hệ phương trình: ",a)
    b = tinh_gioi_han()
    print ("Kết quả tính giới hạn: ",b)
    c = tinh_dao_ham()
    print ("Kết quả tính đạo hàm: ",c)
    d = tinh_nguyen_ham()
    print ("Kết quả tính nguyên hàm: ",d)
    e = tinh_tich_phan()
    print ("Kết quả tính tích phân: ",e)
    

if __name__ == "__main__":
    main()




