"Program Kalkulator BMI"

print("Selamat Datang Di Program Kalkulator BMI ( Body Mass Index )")
print("------------------------------------------------------------")

berat_badan = float(input("Masukkan berat badan anda ( kg ): "))
tinggi_badan = float(input("Masukkan tinggi badan anda ( m ): "))
bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal['atas'] = 25*(tinggi_badan**2)

if bmi <= 18.5:
    kategori = "Anda Kekurangan Berat Badan"
elif bmi <= 25:
    kategori = "Nilai BMI Anda Normal"
elif bmi <= 30:
    kategori = "Anda Kelebihan Berat Badan"
else :
    kategori = "Anda Mengalami Obesitas"

print("\n----------------------------------")
print("Hasil Kalkulasi BNI Anda Adalah : ")
print("----------------------------------")
print(f"Nilai BMI Anda adalah {bmi:.2f} kg/m^2")
print(kategori)
print(f"Berat badan yang ideal untuk anda berada dalam rentang {berat_badan_ideal['bawah']:.2f} kg - {berat_badan_ideal['atas']:.2f} kg ")
print("-------------------------------------------")
print("Terima Kasih Sudah Menggunakan Program Ini")
print("-------------------------------------------")