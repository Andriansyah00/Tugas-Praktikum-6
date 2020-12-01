data =[["Japar",80],["Adit",70],["Bayu",90]]
nama_nomor = []

for i in range (len(data)):
    nama_nomor.append(data[i][0])
    i=+1
    i=i

nomor_urut= len(data)
nomor = nomor_urut

def tampilkan():
    print("Daftar nilai mahasiswa")
    for i in range(len(data)):
        print(data[i][0],':',data[i][1])
    i=+1
    i=i

def tambah():
    global nomor
    nama = input("nama : ")
    nilai = int(input('Nilai : '))
    data.append([nama,nilai])
    nama_nomor.append(nama)
    nomor = nomor + 1
    nomor = nomor

def hapus(nama):
    global nomor
    if nama in nama_nomor:
        data.remove(data[nama_nomor.index(nama)])
        nama_nomor.remove(nama)
        nomor = nomor - 1
        nomor = nomor

def ubah(nama):
    n = input("mengubah nama "+nama+" menjadi : " )
    nilai_1= input("mengubah Nilai "+nama+" menjadi : ")
    data[nama_nomor.index(nama)]=[n,nilai_1]
    nama_nomor [nama_nomor.index(nama)] = n

tambah()
hapus("Japar")
ubah("Adit")
tampilkan()