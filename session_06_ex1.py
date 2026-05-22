qty_laptop = 0
qty_phone = 0
qty_tablet = 0

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ KHO =====")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("0. Thoát chương trình")

    choice = input("Nhập lựa chọn: ")

    if choice == "1":

        print("\n===== BÁO CÁO TỒN KHO =====")

        laptop = ""
        for i in range(qty_laptop):
            laptop += "*"
        print("Laptop (" + str(qty_laptop) + "): " + laptop)

        phone = ""
        for i in range(qty_phone):
            phone += "*"
        print("Phone (" + str(qty_phone) + "): " + phone)

        tablet = ""
        for i in range(qty_tablet):
            tablet += "*"
        print("Tablet (" + str(qty_tablet) + "): " + tablet)
    elif choice == "2":

        print("\n===== NHẬP KHO =====")
        print("1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        item = input("Chọn mặt hàng: ")

        while True:

            qty = int(input("Nhập số lượng: "))

            if qty < 0:
                print("Số lượng không hợp lệ, vui lòng nhập lại!")
                continue

            break

        if item == "1":
            qty_laptop += qty
            print("Nhập Laptop thành công")

        elif item == "2":
            qty_phone += qty
            print("Nhập Phone thành công")

        elif item == "3":
            qty_tablet += qty
            print("Nhập Tablet thành công")

        else:
            print("Mặt hàng không hợp lệ")

    elif choice == "3":

        print("\n===== XUẤT KHO =====")
        print("1. Laptop")
        print("2. Phone")
        print("3. Tablet")

        item = input("Chọn mặt hàng: ")

        while True:

            qty = int(input("Nhập số lượng xuất: "))

            if qty < 0:
                print("Số lượng không hợp lệ, vui lòng nhập lại!")
                continue

            break

        if item == "1":

            if qty > qty_laptop:
                print("Không đủ hàng")
            else:
                qty_laptop -= qty
                print("Xuất Laptop thành công")

        elif item == "2":

            if qty > qty_phone:
                print("Không đủ hàng")
            else:
                qty_phone -= qty
                print("Xuất Phone thành công")

        elif item == "3":

            if qty > qty_tablet:
                print("Không đủ hàng")
            else:
                qty_tablet -= qty
                print("Xuất Tablet thành công")

        else:
            print("Mặt hàng không hợp lệ")

    elif choice == "4":

        print("\n===== CẢNH BÁO TỒN KHO =====")

        warning = False

        if qty_laptop < 10:
            print("[CẢNH BÁO] Laptop sắp hết (Chỉ còn", qty_laptop, "sản phẩm)")
            warning = True

        if qty_phone < 10:
            print("[CẢNH BÁO] Phone sắp hết (Chỉ còn", qty_phone, "sản phẩm)")
            warning = True

        if qty_tablet < 10:
            print("[CẢNH BÁO] Tablet sắp hết (Chỉ còn", qty_tablet, "sản phẩm)")
            warning = True

        if warning == False:
            print("Kho đang ổn định")

    elif choice == "0":

        print("Thoát chương trình")
        break

    else:

        print("Lựa chọn không hợp lệ")
       
