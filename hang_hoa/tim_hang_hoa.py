import csv

def tim_hang_hoa(ma_hoac_ten):
    try:
        with open('csv_file/ds_hang_hoa.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ma_hang'] == ma_hoac_ten or row['ten_mat_hang'] == ma_hoac_ten:
                    print(f"Tìm thấy hàng hóa: Mã: {row['ma_hang']}, Tên: {row['ten_mat_hang']}, Hãng sản xuất: {row['hang_san_xuat']}, Số lượng: {row['so_luong']}, Giá: {row['gia_tien']}")
                    return
        print("Không tìm thấy hàng hóa.")
    except FileNotFoundError:
        print("File danh sách hàng hóa không tồn tại.")