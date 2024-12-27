import csv

def them_hang_hoa(ma, ten, hang_sx, so_luong, don_vi, gia, vat, ngay_nhap, han_su_dung):
    try:
        with open('csv_file/ds_hang_hoa.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['ma_hang'] == ma:
                    print("Mã hàng đã tồn tại.")
                    return
        
        with open('csv_file/ds_hang_hoa.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['ma_hang', 'ten_mat_hang', 'hang_san_xuat', 'so_luong', 'don_vi', 'gia_tien', 'vat', 'ngay_nhap', 'han_su_dung'])
            writer.writerow({'ma_hang': ma, 'ten_mat_hang': ten, 'hang_san_xuat': hang_sx, 'so_luong': so_luong, 'don_vi': don_vi, 'gia_tien': gia, 'vat': vat, 'ngay_nhap': ngay_nhap, 'han_su_dung': han_su_dung})
            print("Thêm hàng hóa thành công.")
    except FileNotFoundError:
        print("File danh sách hàng hóa không tồn tại.")