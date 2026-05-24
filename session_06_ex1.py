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

    match choice:

    
        case "1":
            print("\n===== BÁO CÁO TỒN KHO =====")

            print(f"Laptop ({qty_laptop}): " + "*" * qty_laptop)
            print(f"Phone ({qty_phone}): " + "*" * qty_phone)
            print(f"Tablet ({qty_tablet}): " + "*" * qty_tablet)

        case "2":
            print("\n===== NHẬP KHO =====")
            print("1. Laptop")
            print("2. Phone")
            print("3. Tablet")

            item = input("Chọn mặt hàng: ")

            while True:
                qty = int(input("Nhập số lượng: "))
                if qty < 0:
                    print("Số lượng không hợp lệ!")
                    continue
                break

            match item:
                case "1":
                    qty_laptop += qty
                    print("Nhập Laptop thành công")
                case "2":
                    qty_phone += qty
                    print("Nhập Phone thành công")
                case "3":
                    qty_tablet += qty
                    print("Nhập Tablet thành công")
                case _:
                    print("Mặt hàng không hợp lệ")

        case "3":
            print("\n===== XUẤT KHO =====")
            print("1. Laptop")
            print("2. Phone")
            print("3. Tablet")

            item = input("Chọn mặt hàng: ")

            while True:
                qty = int(input("Nhập số lượng xuất: "))

                if qty < 0:
                    print("Số lượng không hợp lệ!")
                    continue

                match item:
                    case "1":
                        if qty > qty_laptop:
                            print("Không đủ hàng")
                        else:
                            qty_laptop -= qty
                            print("Xuất Laptop thành công")
                            break

                    case "2":
                        if qty > qty_phone:
                            print("Không đủ hàng")
                        else:
                            qty_phone -= qty
                            print("Xuất Phone thành công")
                            break

                    case "3":
                        if qty > qty_tablet:
                            print("Không đủ hàng")
                        else:
                            qty_tablet -= qty
                            print("Xuất Tablet thành công")
                            break

                    case _:
                        print("Mặt hàng không hợp lệ")
                        break

        case "4":
            print("\n===== CẢNH BÁO TỒN KHO =====")

            warning = False

            if qty_laptop < 10:
                print(f"[CẢNH BÁO] Laptop sắp hết ({qty_laptop})")
                warning = True

            if qty_phone < 10:
                print(f"[CẢNH BÁO] Phone sắp hết ({qty_phone})")
                warning = True

            if qty_tablet < 10:
                print(f"[CẢNH BÁO] Tablet sắp hết ({qty_tablet})")
                warning = True

            if not warning:
                print("Kho đang ổn định")

        case "0":
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ")
