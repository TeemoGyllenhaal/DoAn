import numpy as np
import random
def ngau_nhien_vector_so_thuc(a,b,c):
    v = np.random.randint(low = a, high = b, size = c)
    return v
def ngau_nhien_ma_tran_so_thuc(a,b,c,m,n):
    v = np.random.randint(low = a, high = b, size = c).reshape(m,n)
    return v
def nhan_dai_luong_vo_huong_vector_va_ma_tran(a,v):
    p = a*v
    print ("Sau khi nhân: ",p)
    return p
def hadamard(a,b):
    h = np.multiply(a,b)
    print ("Sau khi nhân hadamard: ",h)
    return h
def chuyen_vi(a): 
    b = np.transpose(a)
    return b
def nhan_ma_tran(a,b):
    p = np.dot(a,b)
    return p
def main():
    
    a = int(input("Nhập giá trị khoảng đầu: "))
    b = int(input("Nhập giá trị khoảng cuối: "))
    c = int(input("Nhập số lượng phần tử vector: "))
    d = int(input("Nhập số lượng phần tử ma trận: "))
    m = int(input("Nhập số hàng: "))
    n = int(input("Nhập số cột: "))
    
    #1
    v1 = ngau_nhien_vector_so_thuc(a,b,c)
    print ("Vector: ",v1)
    v2 = ngau_nhien_ma_tran_so_thuc(a,b,d,m,n)
    print ("Ma trận: ",v2)
    nhan_dai_luong_vo_huong_vector_va_ma_tran(int(input("Nhập giá trị a nhân vector: ")),v1)
    nhan_dai_luong_vo_huong_vector_va_ma_tran(int(input("Nhập giá trị a nhân ma trận: ")),v2)
    
    #2
    v3 = ngau_nhien_ma_tran_so_thuc(a,b,d,m,n)
    print ("Ma trận A: ",v3)
    v4 = ngau_nhien_ma_tran_so_thuc(a,b,d,m,n)
    print ("Ma trận B: ",v4)
    hadamard(v3,v4)
    v5 = chuyen_vi(v3)
    print ("Chuyển vị ma trận a: ",v5)
    v6 = nhan_ma_tran(v5,v4)
    print ("Sau khi nhân A**T và B: ",v6)
    
if __name__ == "__main__":
    main()
