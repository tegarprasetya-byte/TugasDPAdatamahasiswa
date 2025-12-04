
user_pw = [
    {"username":"Admin","katasandi":"Admin123"}
]

def tambah_mahasiswa():

def lihat_daftar_mahasiswa():

def cari_mahasiswa():

def update_data():

def hapus_data():

def simpan_data():

def baca_data():

kesempatan=3
login = input("Apakah Anda sudah Memiliki akun? (yes/no) :")

if login == "yes":
    while kesempatan >0:
        input_user = input("Masukan Username :").strip().title()
        input_pw = input("Masukan Kata Sandi :").strip().title()
        for k in user_pw:
            if input_user == k["username"] and input_pw == k["katasandi"]:
                print("Anda Berhasil Login!")
                ditemukan = True
                break
        if ditemukan:
            break
        else:
                kesempatan-=1
                print("Username Atau Katasandi Salah!")
    if kesempatan ==0:
        print("Percobaan Login Gagal! Silahkan Refresh Program.")
elif login == "no":
    print("====== Buat Akun baru ======")
    buat_user = input("Buat Username Baru :").strip().title()
    buat_pw = input("Buat Kata Sandi Baru :").strip().title()
    for k in user_pw:
        user_pw.append({"username":buat_user, "katasandi":buat_pw})
        print("Akun Berhasil Terdaftarkan!\n")
        break
    while kesempatan >0:
        print("===== Login =====")
        input_user = input("Masukan Username :").strip().title()
        input_pw = input("Masukan Kata Sandi :").strip().title()
        for k in user_pw:
            if input_user == k["username"] and input_pw == k["katasandi"]:
                print("Anda Berhasil Login!")
                ditemukan = True
                break
        if ditemukan:
            break
        else:
                kesempatan-=1
                print("Username Atau Katasandi Salah!")
    if kesempatan ==0:
        print("Percobaan Login Gagal! Silahkan Refresh Program.")
            
while True:
    print("\n===== Manajemen Data Mahasiswa =====")
    print("1. Tambah Mahasiswa")
    print("2. Lihat Daftar Mahasiswa")
    print("3. Cari Mahasiswa")
    print("4. Update Data Mahasiswa")
    print("5. Hapus Mahasiswa")
    print("6. Simpan data Mahasiswa")
    print("7. Baca Data Mahasiswa")
    print("8. Keluar")
    pilihan = input("Masukan Pilihan (1-8) :")
    if pilihan == "1":
        tambah_mahasiswa()
    elif pilihan =="2":
        lihat_daftar_mahasiswa()
    elif pilihan =="3":
        cari_mahasiswa()
    elif pilihan =="4":
        update_data()
    elif pilihan=="5":
        hapus_data()
    elif pilihan =="6":
        simpan_data()
    elif pilihan =="7":
        baca_data()
    elif pilihan == "8":
        break
