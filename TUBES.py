# ============================================================
# program  Manajemen Fashion dan Outfit Harian (OOTD Planner) 
# ============================================================

lemari = [
    {
        "id" : 1,
        "nama_pakaian" : "Jersey",
        "kategori_pakaian" : "Sporty",
        "warna" : "Putih",
        "formalitas" : 3,
        "tanggal" : 20260101
    },
    {
        "id" : 2,
        "nama_pakaian" : "Kaos putih",
        "kategori_pakaian" : "Casual",
        "warna" : "Putih",
        "formalitas" : 2,
        "tanggal" : 20260122
    },
    {
        "id" : 3,
        "nama_pakaian" : "Kemeja Putih",
        "kategori_pakaian" : "Formal",
        "warna" : "Putih",
        "formalitas" : 8,
        "tanggal" : 20260304
    },
    {
        "id" : 4,
        "nama_pakaian" : "Celana Chino",
        "kategori_pakaian" : "Casual",
        "warna" : "Cream",
        "formalitas" : 6,
        "tanggal" : 20260608
    },
    {
        "id" : 5,
        "nama_pakaian" : "Kemeja Batik",
        "kategori_pakaian" : "Formal",
        "warna" : "Cokelat",
        "formalitas" : 7,
        "tanggal" : 20260708
    }
]

# ============================================================
# Menampilkan isi lemari
# ============================================================
def lihat_lemari(data = None):
    if data is None:
        data = lemari
    if len(data) == 0:
        print("\n [!] Lemari kosong dan data tidak ditemukan")
        return

    print("\n                          ===== DAFTAR PAKAIAN =====")

    print(f"{'ID':<6} {'nama_pakaian':<20} {'kategori_pakaian':<20} {'warna':<10} {'formalitas':<12} {'tanggal':<12}")

    print("=" * 90)

    for baju in data:
        print(
            f"{baju['id']:<6} "
            f"{baju['nama_pakaian']:<20} "
            f"{baju['kategori_pakaian']:<20} "
            f"{baju['warna']:<10} "
            f"{baju['formalitas']:<12} "
            f"{baju['tanggal']:<12} "
        )

# ============================================================
# Tambah Pakaian
# ============================================================
def tambah_pakaian():
    print("\n                          ===== TAMBAH PAKAIAN =====")

    nama = input("nama_pakaian : ")
    kategori = input("kategori_pakaian : ")
    warna = input("Warna : ")
    formalitas = int(input("Formalitas : "))
    tanggal = int(input("Tanggal dalam format (YYYYMMDD) : "))

    id_baru = lemari[-1]['id'] + 1 if lemari else 1

    data_baru = {
        "id" : id_baru,
        "nama_pakaian" : nama,
        "kategori_pakaian" : kategori,
        "warna" : warna,
        "formalitas" : formalitas,
        "tanggal" : tanggal 
    }

    lemari.append(data_baru)

    print("\n[OK] Pakaian berhasil ditambahkan")

# ============================================================
# EDIT PAKAIAN
# ============================================================
def edit_pakaian():
    lihat_lemari()
    edit_id = int(input("\n Masukkan ID yang ingin diedit : "))

    for baju in lemari :
        if baju['id'] == edit_id:
            print("\n Masukkan data id pakaian yang baru : ")

            baju["nama_pakaian"] = input("Nama baju baru : ")
            baju["kategori_pakaian"] = input("Kategori baru : ")
            baju["warna"] = input("Warna baru : ")
            baju["formalitas"] = int(input("Level baru : "))
            baju["tanggal"] = int(input("Tanggal baru : "))

            print("\n[OK] Data berhasil diubah")
            return

    print("\n [!] ID tidak ditemukan dan tidak terdaftar")

# ============================================================
# HAPUS PAKAIAN
# ============================================================
def hapus_pakaian():
    lihat_lemari()
    hapus_id = int(input("\n Masukkan ID yang ingin dihapus : "))

    for baju in lemari:
        if baju['id'] == hapus_id:
            lemari.remove(baju)
            print("\n[OK] Baju berhasil dihapus")
            return
    print("\n[i] ID Tidak Ditemukan")