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
    6. Tìm tên Laptop. 
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

        elif select == 3:
            id = input("Nhập ID Laptop: ")
            for i in ds :
                if i.get_id() == id:
                    ds.remove(i)
                    print("Bạn đã xóa Laptop thành công!")
                else:
                    print("Bạn Nhập sai ID laptop! Vui lòng nhập lại!")

        elif select == 2:
            id = input("Nhập ID laptop cần sửa : ")
            for i in ds:
                if i.get_id() == id:
                    i.set_Name( input ("Nhập tên mới : "))
                    i.show_info()
        
        elif select == 4 :
            if len(ds) == 0:
                print("\n Hiện không có dữ liệu! Bạn vui lòng thêm Laptop!")
            else:
                print(f"\n Hiện trong kho có {len(ds)} Laptop")
                for i in ds :
                    i.show_info() 

        elif select == 5 :
            id = input("Nhập ID Laptop xem thông tin : ")
            for i in ds:
                if i.get_id() == id:
                    i.show_info()


        elif select == 6:
            name = input("Nhập Tên Laptop xem thông tin : ")
            for i in ds:
                if i.get_Name() == name:
                    i.show_info()

        elif select == 7 :
            print(f"Hiện có {len(ds)} Laptop \n")

    else:
        print(" Số là cách nhập hợp lệ! Bạn vui lòng nhập lại!")