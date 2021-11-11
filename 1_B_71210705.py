nama = input("Nama: ")
lahir = input("Tempat tanggal lahir : ")

a = nama.split()
b = lahir.split()

if len(a) > 2:
    print("Haloo!", a[2], ",", a[0], a[1])
else:
    print("Haloo!", a[1], ",", a[0])

print("Anda lahir di", b[0], "pada tanggal", b[1], b[2], b[3])