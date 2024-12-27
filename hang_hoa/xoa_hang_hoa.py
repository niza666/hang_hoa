import csv

def xoa_hang_hoa(ma):
    try:
        rows = []
        with open('csv_file/ds_hang_hoa.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ma_hang'] != ma:
                    rows.append(row)
                else:
                    print(f"Đã xóa hàng hóa: {row['ten_mat_hang']}")
        
        with open('csv_file/ds_hang_hoa.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ma_hang', 'ten_mat_hang', 'hang_san_xuat', 'so_luong', 'don_vi', 'gia_tien', 'vat', 'ngay_nhap', 'han_su_dung'])
            writer.writeheader()
            writer.writerows(rows)
    except FileNotFoundError:
        print("File danh sách hàng hóa không tồn tại.")