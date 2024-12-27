import csv

def sua_hang_hoa(ma, ten_moi, hang_sx_moi, gia_moi, so_luong_moi):
    try:
        rows = []
        with open('csv_file/ds_hang_hoa.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ma_hang'] == ma:
                    row['ten_mat_hang'] = ten_moi
                    row['hang_san_xuat'] = hang_sx_moi
                    row['gia_tien'] = gia_moi
                    row['so_luong'] = so_luong_moi
                    print(f"Đã cập nhật hàng hóa: {ten_moi}")
                rows.append(row)
        
        with open('csv_file/ds_hang_hoa.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ma_hang', 'ten_mat_hang', 'hang_san_xuat', 'so_luong', 'don_vi', 'gia_tien', 'vat', 'ngay_nhap', 'han_su_dung'])
            writer.writeheader()
            writer.writerows(rows)
    except FileNotFoundError:
        print("File danh sách hàng hóa không tồn tại.")