import csv

def xem_danh_sach_hang_hoa():
    print("=== DANH SÁCH HÀNG HÓA ===")
    try:
        with open('csv_file/ds_hang_hoa.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"Mã kho: {row['ma_kho']}, Mặt hàng: {row['ten_mat_hang']}, Số lượng: {row['so_luong']}")
    except FileNotFoundError:
        print("File danh sách hàng hóa không tồn tại.")