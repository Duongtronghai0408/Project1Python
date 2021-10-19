class Laptop:
    count = 0
    def __init__(self , id , name):
        self.id = id
        self.name = name
        Laptop.count += 1

    #def set_id(self, id):
    #   self.id = id

    def get_id(self):
        return self.id

    def set_Name(self, name):
        self.name = name

    def get_Name(self):
        return self.name

    def show_info(self):
        print(f"Id : {self.get_id()}")
        print(f"Tên Laptop : {self.name}")

Lt = Laptop("Msi01" , "Laptop MSI EK810")

Lt.show_info()
print(Lt.count)