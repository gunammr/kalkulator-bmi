"Program Kalkulator BMI"
#batas bawah : 18.5
#batas atas : 25

print("Selamat Datang Di Program Kalkulator BMI ( Body Mass Index )")
print("------------------------------------------------------------")

berat_badan = float(input("Masukkan berat badan anda ( kg ): "))
tinggi_badan = float(input("Masukkan tinggi badan anda ( m ): "))
bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal['atas'] = 25*(tinggi_badan**2)

print(f"\nNilai BMI anda adalah {bmi:.2f} kg/m^2")
print("Nilai BNI normal berada dalam rentang 18.5 kg/m^2 - 25 kg/m^2")
print(f"Berat badan yang ideal untuk anda berada dalam rentang {berat_badan_ideal['bawah']:.2f} kg - {berat_badan_ideal['atas']:.2f} kg ")
print("-------------------------------------------")
print("Terima Kasih Sudah Menggunakan Program Ini")
print("-------------------------------------------")