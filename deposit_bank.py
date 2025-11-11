# =====================================================
# Program : Kalkulator Deposit Bank
# Deskripsi : Program sederhana untuk mensimulasikan
#             setoran uang dan menghitung saldo akhir.
# =====================================================

def garis():
    print("=" * 50)

def menu():
    print("\n[1] Setor Uang")
    print("[2] Cek Saldo")
    print("[3] Keluar")

def input_setoran():
    """
    Fungsi untuk meminta input jumlah setoran dari pengguna.
    Akan terus meminta hingga input valid (> 0 dan berupa angka).
    """
    while True:
        try:
            jumlah = float(input("Masukkan jumlah setoran (harus > 0): "))
            if jumlah <= 0:
                print("Jumlah setoran tidak boleh nol atau negatif. Coba lagi!\n")
                continue
            return jumlah
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.\n")

def main():
    garis()
    print("      SELAMAT DATANG DI KALKULATOR DEPOSIT BANK ")
    garis()

    # Input nama nasabah
    nama = input("Masukkan nama nasabah: ").strip().title()
    if not nama:
        nama = "Nasabah Tanpa Nama"
    print(f"Selamat datang, {nama}!\n")

    saldo = 0.0  # saldo awal

    # Loop utama program
    while True:
        garis()
        menu()
        garis()
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            # Menu Setor Uang
            print("\n--- Menu Setor Uang ---")
            setoran = input_setoran()
            saldo += setoran
            print(f"Setoran sebesar Rp{setoran:,.2f} berhasil!")
            print(f"Saldo Anda saat ini: Rp{saldo:,.2f}")

        elif pilihan == "2":
            # Menu Cek Saldo
            print("\n--- Menu Cek Saldo ---")
            print(f"Nama Nasabah : {nama}")
            print(f"Saldo Tersimpan : Rp{saldo:,.2f}")
            if saldo == 0:
                print("⚠️ Anda belum melakukan setoran apa pun.")
            elif saldo < 100000:
                print("Saldo Anda masih tergolong kecil. Ayo menabung lebih banyak!")
            else:
                print("Terima kasih telah menabung di Bank Kami!")

        elif pilihan == "3":
            # Menu Keluar
            garis()
            print(f"Terima kasih, {nama}, telah menggunakan layanan kami.")
            print(f"Saldo akhir Anda: Rp{saldo:,.2f}")
            print("Sampai jumpa di lain waktu!")
            garis()
            break

        else:
            print("Pilihan tidak valid! Silakan pilih 1, 2, atau 3.")

# Jalankan program hanya jika file ini dijalankan langsung
if __name__ == "__main__":
    main()
