for employee in range(1, 4):
    print(f"Nhập thông tin nhân viên {employee}: ")
    employee_id = input("Nhập mã nhân viên: ").strip()
    employee_name = input("Nhập họ và tên nhân viên: ").strip()
    department = input("Nhập phòng ban công tác: ")
    if employee_id == "" or employee_name == "":
        print("[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
        break
    print()
    print("--- PHiều Hồ sơ Điện tử ---")
    print(f"Mã Nhân Viên: {employee_id}")
    print(f"Họ Và Tên: {employee_name}")
    print(f"Phòng Ban Công Tác: {department}")
    print()

"""
* Phân tích và thiết kế giải pháp:
- Input: tên nhân viên, mã nhân viên , phòng ban
- Output: mã nhân viên, họ và tên nhân viên, phong ban
"""