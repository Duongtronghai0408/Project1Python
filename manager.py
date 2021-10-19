from Laptop import Laptop


ds = []


while True:
    print(f'''\n
    0. Thoát chương trình.
    1. Thêm Laptop.
    2. Cập nhật thông tin Laptop.
    3. Xóa Laptop.
    4. Xem thông tin tất cả Laptop.
    5. Xem thông tin Laptop
    6. Tìm Laptop. 
    7. Số lượng Laptop đang có.
    ''')
    select = input(" Mời chọn chức năng: ")

    if str(select).isdigit():
        select = int(select)
        if select == 0:
            break
        elif select == 1:
            id = input("Nhập ID Laptop: ")
            name = input("Nhập tên Laptop: ")
            Lt = Laptop(id, name)
            ds.append(Lt)


        elif select == 2:
            id = input("Nhập ID laptop cần sửa : ")
            for i in ds:
                if i.get_id() == id:
                    i.set_Name( input ("Nhập tên mới : "))
                    i.show_info()
        
        elif select ==7:
            print(f"Hiện có {len(ds)} Laptop \n")

    else:
        print(" Số là cách nhập hợp lệ! Bạn vui lòng nhập lại!")