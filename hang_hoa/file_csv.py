import csv

def doc_file_hang_hoa():
    try:
        with open('csv_file/ds_hang_hoa.csv', 'r') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []

def ghi_file_hang_hoa(data):
    with open('csv_file/ds_hang_hoa.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ma_hang', 'ten_mat_hang', 'hang_san_xuat', 'so_luong', 'don_vi', 'gia_tien', 'vat', 'ngay_nhap', 'han_su_dung'])
        writer.writeheader()
        writer.writerows(data)