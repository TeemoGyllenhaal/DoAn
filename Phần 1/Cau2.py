import random
import numpy as np
import pickle
import os
from math import isclose
random.seed(321)

def ngau_nhien_so_thuc(a,b,n):
    x = [(b - a)*random.random() + a for i in range(n)]
    print (x)
    return x

def ngau_nhien_so_thuc_2(a,b,n):
    x = np.random.uniform (a,b,n)
    print (x)
    return x

def ngau_nhien(n):
    x = [random.randint(-5,5) for i in range(n)]
    print (x)
    return x

def sap_xep_giam_dan(x):
    n = len(x)
    for i in range (0, n - 1):
        for j in range (i + 1, n):
            if x[i] < x[j]:
                x[i],x[j] = x[j],x[i]
    print (x)
    return x

def sap_xep_tang_dan(x):
    n = len(x)
    for i in range(0, n - 1):
        for j in range(i+1, n):
            if x[i] > x[j]:
                x[i], x[j] = x[j], x[i]
    print (x)
    return x
    
def tim_kiem_phan_tu(x,n):
    vitri = []
    for i in range(len(x)):
        if isclose(x[i],n):
            vitri.append(i)
    return vitri

def ghi_tap_tin(thu_muc: str, tap_tin: str, sap_xep: str, n: str):
    if n == "vanban":
        try:
            with open (os.path.join(thu_muc, tap_tin), 'w') as f:
                f.write(str(sap_xep))
            print("Kết thúc ghi tập tin")
        except Exception as e:
            print("Lỗi khi ghi tập tin", e)
    else:
        if n == "nhiphan":
            try:
                with open (os.path.join(thu_muc, tap_tin), 'wb') as f:
                    pickle.dump(sap_xep,f)
                print("Kết thúc ghi tập tin")
            except Exception as e:
                print("Lỗi khi ghi tập tin", e)
        else:
            print ("Nhập sai, không thể ghi tập tin ")
            
def main():
    x = ngau_nhien_so_thuc_2(-5,5,10)
    path = 'D:\\data'
    filename = 'Câu 2.txt'
    
    n = str(input("Nhập loại tệp cần ghi 'vanban' hoặc 'nhiphan': "))
    ghi_tap_tin(path,filename,x,n)
    
    m = input("Nhập chiều cần sắp xếp 'True' hoac 'False': ")
    print (m)
    if m == 'True':
        x1 = sap_xep_tang_dan(x)
    elif m == 'False':
        x1 = sap_xep_giam_dan(x)
    else:
        print ("Không thể sắp xếp")
    print (type(x1))
    k = str(input("Nhập loại tệp cần ghi 'vanban' hoặc 'nhiphan': "))
    ghi_tap_tin(path,filename,x1,k)
    
    a = float(input("Nhập số cần tìm: "))
    vitri = tim_kiem_phan_tu(x,a)

    if len(vitri) == 0:
        print ("Không tìm thấy n")
    else:
        print ("Vị trí n: ",vitri)

        
if __name__ == "__main__":
    main()
