from Cau1 import NhanVien
import pickle
import os

def thong_tin(soluong,NhanVien):
    nv = []
    for i in range (soluong):
        hoten, tuoi, luong  = input().split(',')  
        nv.append(NhanVien(hoten,tuoi,luong))       
    return nv

def hien_thi(nv):
    print("Thông tin: ")
    for item in nv:
        print(item)
        
def sap_xep(nv):
    sv = sorted (nv)
    print("Sau khi sắp xếp thông tin giá trị tuổi: ")
    for item in sv:
        print(item)
        
def luu_nhan_vien(dia_chi: str, ten_tap_tin: str, objs: list[NhanVien]):
    try:
        with open (os.path.join(dia_chi, ten_tap_tin), 'wb') as f:
            pickle.dump(objs,f)
        print("Kết thúc ghi tập tin")
    except Exception as e:
        print("Lỗi khi ghi tập tin", e)

def doc_nhan_vien(dia_chi: str, ten_tap_tin: str)-> list[NhanVien]:
    try:
        with open (os.path.join(dia_chi, ten_tap_tin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None
    
def in_list_nhan_vien (s: list[NhanVien]):
    for i in s:
        print(i)

def main():
    
    soluong = int(input("Nhập số lượng nhân viên: "))
    nv = thong_tin(soluong,NhanVien)
    hien_thi(nv)
    sap_xep(nv)
    dia_chi = str(input("Nhập địa chỉ tập tin: "))
    ten_tap_tin = str(input("Nhập tên tập tin: "))
    luu_nhan_vien(dia_chi,ten_tap_tin,nv)
    noi_dung = doc_nhan_vien(dia_chi,ten_tap_tin)
    in_list_nhan_vien(noi_dung)
    print('Kết thúc chương trình')
    
if __name__ == '__main__':
    main()
