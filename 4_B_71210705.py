print("====GEBYAR DISKON====") 
print("====MASUKAN JUMLAH BARANG YANG DIPESAN====")

a = int(input("KIPAS ANGIN DISKON 10%   RP 25.000,00    : ")) 
b = int(input("SEPEDA DISKON 55%        RP 6.000,00     : ")) 
c = int(input("HELM ROSSI DISKON 77%    RP 8.000,00     : ")) 

print("====TOTAL====")

TKA = (10/100) * 25000 * a 
TSP = (55/100) * 6000 * b  
HRD = (77/100) * 8000 * c

print("TOTAL KIPAS ANGIN           :    RP",int(TKA),".0")
print("TOTAL SEPEDA SUPER          :    RP",int(TSP),".0")
print("TOTAL HELM ROSSI            :    RP",int(HRD),".0")

total = TKA + TSP + HRD

print("Jumlah total diskon yang didapat adalah RP",float(total))