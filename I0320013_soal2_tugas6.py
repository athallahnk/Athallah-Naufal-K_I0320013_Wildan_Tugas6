i, n, x, jumlah= 0,0,0,0
ratarata = float

n = int(input("masukkan banyaknya nilai:"))

for i in range (0,n):
    x= int(input("nilai:"))
    jumlah += x
print("jumlah nilai:", jumlah)
ratarata= jumlah/n
print("nilai rata-rata:", ratarata)


