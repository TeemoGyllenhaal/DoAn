class NhanVien:
    def __init__(self,fullname,age,salary):
        self.hoten = fullname
        self.tuoi = age
        self.luong = salary
    def __str__(self):
        message = '[hoten: '+ self.hoten +'; tuoi: '+ str(self.tuoi)+'; luong: '+ str(self.luong) +']'
        return message
    def __gt__(self,obj):
        return (self.tuoi>obj.tuoi)
    def __ge__(self,obj):
        return (self.tuoi>=obj.tuoi)
    def __lt__(self,obj):
        return (self.tuoi<obj.tuoi)
    def __le__(self,obj):
        return (self.tuoi<=obj.tuoi)
    def __eq__(self,obj):
        return (self.tuoi==obj.tuoi)