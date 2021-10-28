class Laptop:
    count = 0
    def __init__(self , id , name , kho, gia):
        self.id = id
        self.name = name
        self.kho = kho
        self.gia = gia
        Laptop.count += 1

    #def set_id(self, id):
    #   self.id = id

    def get_id(self):
        return self.id

    def set_Name(self, name):
        self.name = name

    def get_Name(self):
        return self.name
    
    def set_Kho(self, kho):
        self.kho = kho

    def get_Kho(self):
        return self.kho

    def set_Gia(self, gia):
        self.gia = gia

    def get_Gia(self):
        return self.gia


    def show_info(self):
        print(f"\n Thông tin của Laptop ")
        print(f"Id : {self.get_id()}")
        print(f"Tên Laptop : {self.name}")
        print(f"Tồn Kho : {self.kho}")
        print(f"Thành Giá : {self.gia}")

