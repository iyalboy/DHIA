# perulangan
# for-loop
'''
    for-loop digunakan untuk perulangan yang di ketahui jumlah perulangannya counted-loop
    
    syntax:
    for kondisi:
         aksi 1 - bagian dari loop
    aksi 2 - bukan bagian dari loop
'''

a = 0
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)
a += 1
print(a)
# boros line of code

angka = [0,1,5,7,10]
for i in angka:
    print(f"i saat ini -> {i}")
print ("ini akhir dari loop")

# perulangan menggunakan range
angka_range = range(5) # di ulang 5 kali

for i in angka_range:
    print(f"i saat ini -> {i}")
print ("ini akhir dari loop 2\n")

angka_range = range(1,10) # di ulang 9 kali

for i in angka_range:
    print(f"i saat ini -> {i}")
print ("ini akhir dari loop 2\n")

string = "mandalika"
print(string)

for huruf in string:
    print(huruf)
print ("ini akhir dari loop 4\n")