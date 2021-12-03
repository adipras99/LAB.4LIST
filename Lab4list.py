#variabel berulang
list_nama=[]
list_nim=[]
list_tugas=[]
list_uts=[]
list_uas=[]
list_akhir=[]

#program
ulang=int(input("masukan data mahasiswa"))
for i in range(ulang):
    print("data ke " +str(i+1))
    list_nama.append(input("masukan nama"))
    list_nim.append(input("masukan nim"))
    list_tugas.append(int(input("masukan nialai tugas")))
    list_uts.append(int(input("masukan nilai uts")))
    list_uas.append(int(input("masukan nilai uas")))

#nilai akhir
for i in range(ulang):
    list_akhir.append(int(list_tugas[i])*0.30 + (int(list_uts[i])*0.30 + (int(list_uas[i])*0.35)))
#cetak program
print("=================================================================================")
print(" nama    nim     nilai tugas     nilai uts       nilai uas             akhir    ")
print("==================================================================================")

for i in range(ulang):
    print("%s \t %s \t\t %i \t\t\t %i \t\t\t\ %i \t\t\t\t %i \t\t\t\t\t" %
          (list_nama[i],list_nim[i],list_tugas[i],list_uts[i],list_uas[i],list_akhir[i]))
print("==================================================================================")

