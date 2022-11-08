import random

operasi = ["Pertambahan", "Pengurangan", "Perkalian", "Pembagian"]
jumlahBenar = 0
numberA = 0
numberB = 0
inputSoal = 0
jawaban = 0
pilihOperasi = 0

# Menu
jumlahSoal = int(input("Masukan Jumlah Soal : "))
print("Pilih Jenis Soal:")
print("1. Hanya Pertambahan")
print("2. Hanya Pengurangan")
print("3. Hanya Perkalian")
print("4. Hanya Pembagian")
print("5. Soal Campur")
jenisSoal = int(input("Masukan Jenis Soal : "))
print("\n")
if jenisSoal < 0 or jenisSoal > 5:
    print("Jenis Soal Tidak Ada!")
else:
    for i in range(jumlahSoal):
        # Jenis Soal
        if jenisSoal == 5:
            pilihOperasi = random.randint(0,3)
        else:
            pilihOperasi = (jenisSoal-1)

        # Proses Soal
        if operasi[pilihOperasi] == "Pertambahan":
            numberA = random.randint(1,20)
            numberB = random.randint(1,20)
            inputSoal = int(input(str(numberA) + " + " + str(numberB) + " = "))
            jawaban = numberA + numberB
        elif operasi[pilihOperasi] == "Pengurangan":
            numberA = random.randint(15,40)
            numberB = random.randint(1,15)
            inputSoal = int(input(str(numberA) + " - " + str(numberB) + " = "))
            jawaban = numberA - numberB
        elif operasi[pilihOperasi] == "Perkalian":
            numberA = random.randint(1,10)
            numberB = random.randint(1,5)
            inputSoal = int(input(str(numberA) + " x " + str(numberB) + " = "))
            jawaban = numberA * numberB
        elif operasi[pilihOperasi] == "Pembagian":
            numberA = random.randint(3,15)
            numberB = random.randint(3,10)
            inputSoal = int(input(str(numberA*numberB) + " : " + str(numberA) + " = "))
            jawaban = numberB

        # Cek Jawaban
        if inputSoal == jawaban:
            print("Benar")
            jumlahBenar += 1
        else:
            print("Salah")
    # Hasil
    print("Total Soal : " + str(jumlahSoal) + " | " + "Total Benar : " + str(jumlahBenar) + " | Total Salah : " + str((jumlahSoal - jumlahBenar)))