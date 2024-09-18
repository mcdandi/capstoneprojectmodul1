from tabulate import tabulate

# Data Karyawan Inisiasi Awal
employees = [
    {"ID": "EMP001", "Nama": "Budi Santoso", "Jabatan": "Manager", "Gaji": 15000000, "Departemen": "HR", "Tanggal Bergabung": "12-05-2019", "Gender": "Pria", "Email": "budi.santoso@purwadhika.com"},
    {"ID": "EMP002", "Nama": "Agus Wirawan", "Jabatan": "Staff", "Gaji": 7500000, "Departemen": "Finance", "Tanggal Bergabung": "23-08-2020", "Gender": "Pria", "Email": "agus.wirawan@purwadhika.com"},
    {"ID": "EMP003", "Nama": "Siti Rahma", "Jabatan": "Supervisor", "Gaji": 10000000, "Departemen": "Marketing", "Tanggal Bergabung": "17-03-2018", "Gender": "Wanita", "Email": "siti.rahma@purwadhika.com"},
    {"ID": "EMP004", "Nama": "Dewi Susanti", "Jabatan": "Staff", "Gaji": 8000000, "Departemen": "IT", "Tanggal Bergabung": "05-11-2021", "Gender": "Wanita", "Email": "dewi.susanti@purwadhika.com"},
    {"ID": "EMP005", "Nama": "Budi Sudarsono", "Jabatan": "Manager", "Gaji": 16000000, "Departemen": "Finance", "Tanggal Bergabung": "09-07-2017", "Gender": "Pria", "Email": "budi.sudarsono@purwadhika.com"},
    {"ID": "EMP006", "Nama": "Ahmad Zulkifli", "Jabatan": "Staff", "Gaji": 7000000, "Departemen": "Marketing", "Tanggal Bergabung": "14-02-2021", "Gender": "Pria", "Email": "ahmad.zulkifli@purwadhika.com"},
    {"ID": "EMP007", "Nama": "Sri Rahayu", "Jabatan": "Supervisor", "Gaji": 11000000, "Departemen": "IT", "Tanggal Bergabung": "21-06-2016", "Gender": "Wanita", "Email": "sri.rahyu@purwadhika.com"},
    {"ID": "EMP008", "Nama": "Budi Prasetyo", "Jabatan": "Staff", "Gaji": 7200000, "Departemen": "HR", "Tanggal Bergabung": "12-01-2020", "Gender": "Pria", "Email": "budi.prasetyo@purwadhika.com"},
    {"ID": "EMP009", "Nama": "Eka Saputra", "Jabatan": "Manager", "Gaji": 15500000, "Departemen": "IT", "Tanggal Bergabung": "09-09-2015", "Gender": "Pria", "Email": "eka.saputra@purwadhika.com"},
    {"ID": "EMP010", "Nama": "Nurul Aini", "Jabatan": "Staff", "Gaji": 7800000, "Departemen": "Marketing", "Tanggal Bergabung": "18-10-2019", "Gender": "Wanita", "Email": "nurul.aini@purwadhika.com"},
    {"ID": "EMP011", "Nama": "Budi Mulyono", "Jabatan": "Staff", "Gaji": 7200000, "Departemen": "HR", "Tanggal Bergabung": "20-07-2021", "Gender": "Pria", "Email": "budi.mulyono@purwadhika.com"},
    {"ID": "EMP012", "Nama": "Maya Sari", "Jabatan": "Manager", "Gaji": 15500000, "Departemen": "Finance", "Tanggal Bergabung": "12-12-2016", "Gender": "Wanita", "Email": "maya.sari@purwadhika.com"},
    {"ID": "EMP013", "Nama": "Andi Setiawan", "Jabatan": "Supervisor", "Gaji": 12000000, "Departemen": "IT", "Tanggal Bergabung": "03-04-2017", "Gender": "Pria", "Email": "andi.setiawan@purwadhika.com"},
    {"ID": "EMP014", "Nama": "Nina Wulandari", "Jabatan": "Staff", "Gaji": 7900000, "Departemen": "Marketing", "Tanggal Bergabung": "01-05-2018", "Gender": "Wanita", "Email": "nina.wulandari@purwadhika.com"},
    {"ID": "EMP015", "Nama": "Rudi Hidayat", "Jabatan": "Supervisor", "Gaji": 11500000, "Departemen": "Finance", "Tanggal Bergabung": "14-08-2015", "Gender": "Pria", "Email": "rudi.hidayat@purwadhika.com"},
    {"ID": "EMP016", "Nama": "Rina Amalia", "Jabatan": "Staff", "Gaji": 7300000, "Departemen": "HR", "Tanggal Bergabung": "29-06-2019", "Gender": "Wanita", "Email": "rina.amalia@purwadhika.com"},
    {"ID": "EMP017", "Nama": "Eko Prabowo", "Jabatan": "Manager", "Gaji": 16000000, "Departemen": "IT", "Tanggal Bergabung": "25-12-2017", "Gender": "Pria", "Email": "eko.prabowo@purwadhika.com"},
    {"ID": "EMP018", "Nama": "Lina Kurnia", "Jabatan": "Staff", "Gaji": 7500000, "Departemen": "Marketing", "Tanggal Bergabung": "14-11-2018", "Gender": "Wanita", "Email": "lina.kurnia@purwadhika.com"},
    {"ID": "EMP019", "Nama": "Faisal Arif", "Jabatan": "Supervisor", "Gaji": 10800000, "Departemen": "HR", "Tanggal Bergabung": "19-02-2016", "Gender": "Pria", "Email": "faisal.arif@purwadhika.com"},
    {"ID": "EMP020", "Nama": "Ayu Lestari", "Jabatan": "Staff", "Gaji": 7400000, "Departemen": "Finance", "Tanggal Bergabung": "02-09-2020", "Gender": "Wanita", "Email": "ayu.lestari@purwadhika.com"},
]

# Fungsi untuk menampilkan tabel karyawan
def display_employees(employees):
    headers = ["ID", "Nama", "Jabatan", "Gaji", "Departemen", "Tanggal Bergabung", "Gender", "Email"]
    table = [[e["ID"], e["Nama"], e["Jabatan"], f"Rp {e['Gaji']:,}", e["Departemen"], e["Tanggal Bergabung"], e["Gender"], e["Email"]] for e in employees]
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

#### VALIDASI INPUT ###
# Fungsi untuk validasi id karyawan
def validate_id(id_karyawan):
    id_karyawan = id_karyawan.upper()
    
    # Cek apakah format ID sesuai (EMPxxx) dan angka di bagian belakang lebih dari 000
    if len(id_karyawan) == 6 and id_karyawan[:3] == "EMP" and id_karyawan[3:].isdigit():
        # Konversi bagian numerik menjadi integer untuk memeriksa nilainya
        nomor_id = int(id_karyawan[3:])
        
        if nomor_id == 0:  # Jika ID adalah EMP000, tolak
            print("ID Karyawan tidak boleh EMP000")
            return None
        if any(e["ID"] == id_karyawan for e in employees):
            print("ID Karyawan sudah ada.")
            return None
        return id_karyawan
    else:
        print("Format ID harus EMPxxx.")
        return None

# Fungsi untuk validasi nama, jabatan, atau departemen
def validate_name(input_str):
    if all(char.isalpha() or char.isspace() for char in input_str):  # Memastikan input hanya berisi huruf dan spasi
        return input_str.title()  # Mengubah huruf pertama tiap kata menjadi huruf besar
    else:
        print("Input hanya boleh berisi huruf dan spasi.")
        return None

# Fungsi untuk validasi gaji
def validate_gaji(gaji):
    try:
        gaji = int(gaji)
        if gaji > 0:
            return gaji
        else:
            print("Gaji harus lebih dari 0.")
            return None
    except ValueError:
        print("Gaji harus berupa angka.")
        return None

# Fungsi untuk validasi tanggal
def validate_tanggal(tanggal):
    if len(tanggal) == 10 and tanggal[2] == "-" and tanggal[5] == "-":
        day, month, year = tanggal.split("-")
        if day.isdigit() and month.isdigit() and year.isdigit():
            if 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and len(year) == 4:
                return tanggal
    print("Format tanggal tidak valid. Harus DD-MM-YYYY.")
    return None

# Fungsi untuk validasi gender
def validate_gender(gender):
    gender = gender.strip().lower()  # Menghapus spasi di awal/akhir dan ubah ke huruf kecil
    if gender == "pria" or gender == "wanita":
        return gender.title()  # Mengembalikan 'Pria' atau 'Wanita' dalam kapital
    else:
        print("Gender tidak valid. Harus 'Pria' atau 'Wanita'.")
        return None

# Fungsi validasi email
def validate_email(email):
    if not email:
        return "Alamat Email tidak diisi"

    # Pastikan hanya ada satu '@'
    if "@" not in email or email.count("@") != 1:
        return "Email Tidak Valid, Alasan: Format Email Salah"

    username, domain = email.split("@")

    # Validasi username
    if len(username) == 0:
        return "Email Tidak Valid, Alasan: Username tidak boleh kosong"

    # Username harus diawali dengan huruf atau angka
    if not username[0].isalnum():
        return "Email Tidak Valid, Alasan: Username harus diawali huruf atau angka"

    # Karakter yang diperbolehkan untuk username: huruf, angka, titik, dan underscore
    for char in username:
        if not (char.isalnum() or char in "._"):
            return "Email Tidak Valid, Alasan: Username hanya boleh mengandung huruf, angka, titik, atau underscore"

    # Tidak boleh ada titik di awal atau akhir username, serta tidak boleh ada dua titik berturut-turut
    if username.startswith(".") or username.endswith(".") or ".." in username:
        return "Email Tidak Valid, Alasan: Format Username yang Anda masukkan salah"

    # Validasi domain
    if len(domain) == 0:
        return "Email Tidak Valid, Alasan: Domain tidak boleh kosong"

    # Domain harus tepat "purwadhika.com"
    if domain != "purwadhika.com":
        return "Email Tidak Valid, Alasan: Format Hosting yang Anda masukkan salah"

    # Domain harus memiliki setidaknya satu titik
    if "." not in domain:
        return "Email Tidak Valid, Alasan: Format Ekstensi yang Anda masukkan salah"

    # Ekstensi setelah titik harus minimal 2 karakter
    domain_name, extension = domain.rsplit(".", 1)
    if len(extension) < 2:
        return "Email Tidak Valid, Alasan: Ekstensi domain tidak valid"

    return "Alamat Email yang Anda masukkan valid"

# Fungsi untuk meng-generate email dari nama karyawan
def generate_email_from_name(name):
    name_parts = name.split()  # Memisahkan nama berdasarkan spasi
    if len(name_parts) == 1:
        # Jika hanya ada satu nama, gunakan nama tersebut dua kali
        email = f"{name_parts[0].lower()}.{name_parts[0].lower()}@purwadhika.com"
    else:
        # Jika lebih dari satu nama, gunakan nama pertama dan nama terakhir
        email = f"{name_parts[0].lower()}.{name_parts[-1].lower()}@purwadhika.com"
    return email

def show_email_requirements():
    print("\n=== Persyaratan Email yang Valid ===")
    print("Jika anda memilih 'Generate email karyawan otomatis' maka:")
    print("- Jika nama hanya terdiri dari satu nama, maka format email nya adalah nama.nama@purwadhika")
    print("- Jika nama lebih dari satu nama, maka format email nya adalah nama_awal.nama_akhir@purwadhika.com")
    print("- Email tidak boleh sama dengan email karyawan yang lain\n")
    print("Jika anda memilih 'Custom email karyawan' maka:")
    print("- Format harus 'NamaUser@purwadhika.com'")
    print("- Nama user hanya boleh huruf, angka, underscore (_) dan dot (.)")
    print("- Nama user hanya boleh diawali huruf atau angka")
    print("- Karakter khusus selain underscore dan dot tidak diperbolehkan")
    print("- Hanya diperbolehkan satu '@'")
    print("- Ekstensi harus '@purwadhika.com'")
    print("- Jika nama hanya terdiri dari satu nama, maka nama.nama@purwadhika")
    print("- Jika nama lebih dari satu nama, maka nama_awal.nama_akhir@purwadhika.com")
    print("- Email tidak boleh sama dengan email karyawan yang lain\n")

# Fungsi pengisian tidak boleh kosong
def validate_non_empty(input_str):
    return input_str.strip() != ""

# Fungsi konfirmasi penyimpanan
def confirm_save():
    while True:
        confirm = input("Apakah data akan disimpan (Y/N)? ").strip().lower()
        if confirm == 'y':
            print("Data berhasil disimpan!")
            return True
        elif confirm == 'n':
            print("Data tidak disimpan.")
            return False
        else:
            print("Input tidak valid. Harap masukkan Y atau N.")

# Fungsi konfirmasi penghapusan
def confirm_delete():
    while True:
        confirm = input("Apakah data akan dihapus (Y/N)? ").strip().lower()
        if confirm == 'y':
            print("Data berhasil dihapus!")
            return True
        elif confirm == 'n':
            print("Data tidak dihapus.")
            return False
        else:
            print("Input tidak valid. Harap masukkan Y atau N.")

### READ ###
## Fungsi untuk melihat karyawan (dengan sub-fitur Lihat seluruh karyawan, Cari, dan Urutkan)
def view_employees():
    while True:
        print("\n=== Lihat Karyawan ===")
        print("1. Lihat seluruh karyawan")
        print("2. Cari karyawan tertentu")
        print("3. Urutkan karyawan berdasarkan nama atau gaji")
        print("4. Kembali ke menu utama")
        choice = input("Pilih opsi (1/2/3/4): ")

        if choice == "1":
            display_employees(employees)
        elif choice == "2":
            search_employee()
        elif choice == "3":
            sort_employees()
        elif choice == "4":
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Fungsi untuk mencari karyawan
def search_employee():
    print("\n=== Pencarian Karyawan ===")
    print("Pilih kriteria pencarian:")
    print("1. ID Karyawan")
    print("2. Nama")
    print("3. Jabatan")
    print("4. Gaji")
    print("5. Gender")
    print("6. Tanggal Bergabung")
    print("7. Email")
    print("8. Kembali ke menu utama")
    
    choice = input("Pilih opsi (1-8): ")
    results = []

    if choice == "1":
        keyword = input("Masukkan ID Karyawan untuk mencari: ").upper()
        results = [e for e in employees if keyword in e["ID"].upper()]
    
    elif choice == "2":
        keyword = input("Masukkan Nama untuk mencari: ").lower()
        results = [e for e in employees if keyword in e["Nama"].lower()]
    
    elif choice == "3":
        keyword = input("Masukkan Jabatan untuk mencari: ").lower()
        results = [e for e in employees if keyword in e["Jabatan"].lower()]
    
    elif choice == "4":
        keyword = input("Masukkan Gaji untuk mencari: ")
        results = [e for e in employees if keyword in str(e["Gaji"])]
    
    elif choice == "5":
        keyword = input("Masukkan Gender untuk mencari: ").title()
        results = [e for e in employees if keyword == e["Gender"].title()]
    
    elif choice == "6":
        keyword = input("Masukkan Tanggal Bergabung untuk mencari (DD-MM-YYYY): ")
        results = [e for e in employees if keyword in e["Tanggal Bergabung"]]
    
    elif choice == "7":
        keyword = input("Masukkan Email untuk mencari: ").lower()
        results = [e for e in employees if keyword in e["Email"].lower()]
    
    elif choice == "8":
        return  # Kembali ke menu utama
    
    else:
        print("Pilihan tidak valid.")
        return

    if results:
        display_employees(results)
        print(f"\n{len(results)} employee(s) found.")
    else:
        print("\nKaryawan tidak ditemukan.\n")

# Fungsi untuk mengurutkan karyawan berdasarkan nama atau gaji
def sort_employees():
    print("1. Urutkan Berdasarkan Nama")
    print("2. Urutkan Berdasarkan Gaji")
    choice = input("Pilih metode sorting (1/2): ")
    
    # Urutkan berdasarkan nama
    if choice == "1":
        print("1. Urutkan nama karyawan dari A-Z")
        print("2. Urutkan nama karyawan dari Z-A")
        order = input("Pilih urutan (1/2): ")
        if order == "1":
            sorted_employees = sorted(employees, key=lambda x: x["Nama"])
        elif order == "2":
            sorted_employees = sorted(employees, key=lambda x: x["Nama"], reverse=True)
        else:
            print("Pilihan tidak valid.")
            return
        
    # Urutkan berdasarkan gaji
    elif choice == "2":
        print("1. Dari Gaji Terbesar")
        print("2. Dari Gaji Terkecil")
        order = input("Pilih urutan (1/2): ")
        if order == "1":
            sorted_employees = sorted(employees, key=lambda x: x["Gaji"], reverse=True)
        elif order == "2":
            sorted_employees = sorted(employees, key=lambda x: x["Gaji"])
        else:
            print("Pilihan tidak valid.")
            return
    else:
        print("Pilihan tidak valid.")
        return
    
    display_employees(sorted_employees)

### CREATE ###
# Fungsi untuk menambah karyawan
def create_employee():
    while True:
        print("\n=== Tambah Karyawan ===")
        print("1. Tambah karyawan")
        print("2. Kembali ke menu utama")
        choice = input("Pilih opsi (1/2): ")

        if choice == "1":
            while True:
                display_employees(employees)
                print("\nMasukkan detail karyawan:")

                # input id karyawan
                while True:
                    id_karyawan = input("ID Karyawan (format: EMPxxx): ")
                    id_karyawan = validate_id(id_karyawan)
                    if id_karyawan:
                        break
                    else:
                        print("ID Karyawan tidak valid, silakan ulangi.")

                # input nama
                while True:
                    nama = input("Nama Karyawan: ")
                    if validate_non_empty(nama):
                        nama = validate_name(nama)  # validasi nama harus string
                        if nama:
                            break
                    else:
                        print("Nama tidak boleh kosong, silakan ulangi.")

                # input jabatan
                while True:
                    jabatan = input("Jabatan: ")
                    if validate_non_empty(jabatan):
                        jabatan = validate_name(jabatan)  # validasi jabatan harus string
                        if jabatan:
                            break
                    else:
                        print("Jabatan tidak boleh kosong, silakan ulangi.")

                # input gaji
                while True:
                    gaji = input("Gaji (masukkan angka saja): ")
                    gaji = validate_gaji(gaji)
                    if gaji is not None:
                        break
                    else:
                        print("Gaji tidak valid, silakan ulangi.")

                # input departemen
                while True:
                    departemen = input("Departemen: ")
                    if validate_non_empty(departemen):
                        departemen = validate_name(departemen)  # validasi departemen harus string
                        if departemen:
                            break
                    else:
                        print("Departemen tidak boleh kosong, silakan ulangi.")

                # input tanggal bergabung
                while True:
                    tanggal_bergabung = input("Tanggal Bergabung (DD-MM-YYYY): ")
                    tanggal_bergabung = validate_tanggal(tanggal_bergabung)
                    if tanggal_bergabung is not None:
                        break
                    else:
                        print("Tanggal Bergabung tidak valid, silakan ulangi.")

                # input gender
                while True:
                    gender = input("Jenis kelamin (Pria/Wanita): ")
                    if validate_non_empty(gender):
                        gender = validate_gender(gender)
                        if gender:
                            break
                        else:
                            print("Jenis kelamin tidak valid, hanya 'Pria' atau 'Wanita'.")
                    else:
                        print("Jenis kelamin tidak boleh kosong.")

                # input email
                show_email_requirements()
                while True:
                    print("\nPilih metode input email:")
                    print("1. Generate email karyawan otomatis")
                    print("2. Custom email karyawan")
                    email_choice = input("Pilih opsi (1/2): ")

                    if email_choice == "1":
                        email = generate_email_from_name(nama)
                        if any(e["Email"] == email for e in employees):
                            print("Email karyawan sudah ada, coba pilih yang lain.")
                        else:
                            break  # Email valid dan tidak ada yang sama

                    elif email_choice == "2":
                        email = input("Masukkan Email: ")
                        validation_message = validate_email(email)
                        if any(e["Email"] == email for e in employees):
                            print("Email karyawan sudah ada, coba pilih yang lain.")
                        elif validation_message == "Alamat Email yg anda Masukkan Valid":
                            break  # Email valid dan tidak ada yang sama, keluar dari loop
                        else:
                            print(validation_message)  # Tampilkan pesan kesalahan
                    else:
                        print("Pilihan tidak valid, silakan ulangi.")
                        
                new_employee = {
                    "ID": id_karyawan,
                    "Nama": nama,
                    "Jabatan": jabatan,
                    "Gaji": gaji,
                    "Departemen": departemen,
                    "Tanggal Bergabung": tanggal_bergabung,
                    "Gender": gender,
                    "Email": email
                }
                if confirm_save():
                    employees.append(new_employee)
                    break

        # Fungsi kembali ke menu utama
        elif choice == "2":
            break

        # Fungsi jika pilihan selain 1 atau 2
        else:
            print("Pilihan tidak valid.")

### UPDATE
# Fungsi untuk mengubah informasi karyawan
def update_employee():
    while True:
        print("\n=== Update Karyawan ===")
        print("1. Update karyawan")
        print("2. Kembali ke menu utama")
        choice = input("Pilih opsi (1/2): ")

        if choice == "1":
            display_employees(employees)
            id_karyawan = input("Masukkan ID Karyawan yang akan diupdate: ").upper()  # input id karyawan

            # Pengecekan ID Karyawan
            for e in employees:
                if e["ID"] == id_karyawan:
                    print(f"\nData ditemukan untuk ID {id_karyawan}.")
                    print("Biarkan input kosong jika tidak ingin mengubah data.")

                    # Input nama baru
                    while True:
                        nama = input(f"Nama baru ({e['Nama']}): ")
                        if nama:
                            validated_name = validate_name(nama)
                            if validated_name:
                                e["Nama"] = validated_name
                                break
                            else:
                                print("Nama tidak valid. Silakan ulangi.")
                        else:
                            break  # Tidak ingin mengubah nama

                    # Input jabatan baru
                    while True:
                        jabatan = input(f"Jabatan baru ({e['Jabatan']}): ")
                        if jabatan:
                            validated_jabatan = validate_name(jabatan)
                            if validated_jabatan:
                                e["Jabatan"] = validated_jabatan
                                break
                            else:
                                print("Jabatan tidak valid. Silakan ulangi.")
                        else:
                            break  # Tidak ingin mengubah jabatan

                    # Input gaji baru
                    while True:
                        gaji = input(f"Gaji baru (masukkan angka saja) ({e['Gaji']}): ")
                        if gaji:
                            validated_gaji = validate_gaji(gaji)
                            if validated_gaji is not None:
                                e["Gaji"] = validated_gaji
                                break
                            else:
                                print("Gaji tidak valid. Silakan ulangi.")
                        else:
                            break  # Tidak ingin mengubah gaji

                    # Input departemen baru
                    while True:
                        departemen = input(f"Departemen baru ({e['Departemen']}): ")
                        if departemen:
                            validated_dept = validate_name(departemen)
                            if validated_dept:
                                e["Departemen"] = validated_dept
                                break
                            else:
                                print("Departemen tidak valid. Silakan ulangi.")
                        else:
                            break  # Tidak ingin mengubah departemen

                    # Input tanggal bergabung baru
                    while True:
                        tanggal_bergabung = input(f"Tanggal Bergabung baru ({e['Tanggal Bergabung']}): ")
                        if tanggal_bergabung:
                            validated_tanggal = validate_tanggal(tanggal_bergabung)
                            if validated_tanggal is not None:
                                e["Tanggal Bergabung"] = validated_tanggal
                                break
                            else:
                                print("Tanggal tidak valid. Silakan ulangi.")
                        else:
                            break  # Tidak ingin mengubah tanggal bergabung

                    # Input gender baru
                    while True:
                        gender = input(f"Gender baru ({e['Gender']}): ")
                        if gender:
                            validated_gender = validate_gender(gender)
                            if validated_gender:
                                e["Gender"] = validated_gender
                                break
                            else:
                                print("Gender tidak valid. Silakan ulangi.")
                        else:
                            break  # Tidak ingin mengubah gender

                    # Input email baru
                    while True:
                        show_email_requirements()
                        print("\nPilih metode update email:")
                        print("1. Generate email karyawan otomatis")
                        print("2. Custom email karyawan")
                        print("Tekan Enter tanpa input jika tidak ingin mengubah email.")
                        
                        email_choice = input("Pilih opsi (1/2): ")

                        if email_choice == "1":
                            # Generate email otomatis, boleh sama dengan email sebelumnya jika ID karyawan sama
                            new_email = generate_email_from_name(e["Nama"])
                            
                            # Cek apakah email baru ini sudah digunakan oleh karyawan lain (ID berbeda)
                            if any(e2["Email"] == new_email and e2["ID"] != e["ID"] for e2 in employees):
                                print("Email karyawan sudah digunakan oleh karyawan lain. Coba yang lain.")
                            else:
                                e["Email"] = new_email  # Update email jika valid
                                break  # Keluar dari loop dan lanjut ke penyimpanan

                        elif email_choice == "2":
                            # Input custom email
                            new_email = input("Masukkan Email: ")
                            
                            # Jika dikosongkan, tidak ada perubahan email
                            if not new_email:
                                print("Email tidak diubah.")
                                break
                            
                            # Validasi email baru
                            validation_message = validate_email(new_email)

                            # Jika email valid, update dan keluar dari loop
                            if validation_message == "Alamat Email yang Anda masukkan valid":
                                # Cek apakah email sudah digunakan oleh karyawan lain (ID berbeda)
                                if any(e2["Email"] == new_email and e2["ID"] != e["ID"] for e2 in employees):
                                    print("Email karyawan sudah digunakan oleh karyawan lain. Coba yang lain.")
                                else:
                                    e["Email"] = new_email  # Update email jika valid
                                    break  # Keluar dari loop dan lanjut ke penyimpanan
                            else:
                                # Jika tidak valid, tampilkan pesan kesalahan
                                print(validation_message)

                        elif not email_choice:
                            print("Email tidak diubah.")
                            break  # Jika tidak ada input (Enter ditekan), tidak ada perubahan email

                        else:
                            print("Pilihan tidak valid. Silakan ulangi.")

                    # Setelah keluar dari loop, lanjut ke konfirmasi penyimpanan
                    if confirm_save():
                        print("Data karyawan berhasil diupdate.")
                    else:
                        print("Data karyawan tidak disimpan.")
            else:
                print("ID Karyawan tidak ditemukan.")
        elif choice == "2":
            break
        else:
            print("Pilihan tidak valid.")

### DELETE
# Fungsi untuk menghapus karyawan
def delete_employee():
    while True:
        print("\n=== Hapus Karyawan ===")
        print("1. Hapus karyawan")
        print("2. Kembali ke menu utama")
        choice = input("Pilih opsi (1/2): ")

        if choice == "1":
            display_employees(employees)
            id_karyawan = input("Masukkan ID Karyawan yang akan dihapus: ").upper()

            for e in employees:
                if e["ID"] == id_karyawan:
                    print(f"\nData ditemukan untuk ID {id_karyawan}.")
                    if confirm_delete():
                        employees.remove(e)
                        print(f"Karyawan dengan ID {id_karyawan} berhasil dihapus.")
                    break
            else:
                print("ID Karyawan tidak ditemukan.")
        elif choice == "2":
            break
        else:
            print("Pilihan tidak valid.")

# Menu utama
def main_menu():
    while True:
        print("\n====================== DATA KARYAWAN PT PURWADHIKA ====================")
        print("\n=== Sistem Pengelolaan Karyawan ===")
        print("1. Lihat Karyawan")
        print("2. Tambah Karyawan")
        print("3. Update Karyawan")
        print("4. Hapus Karyawan")
        print("5. Keluar")

        choice = input("Pilih opsi (1/2/3/4/5): ")

        if choice == "1":
            view_employees()
        elif choice == "2":
            create_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Menjalankan program
main_menu()