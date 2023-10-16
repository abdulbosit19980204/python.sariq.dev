mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
ismlar = [] # bo'sh ro'yxat

print(mevalar)
print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])

print("Birinchi meva: ", mevalar[0].title())
print("Ikkinchi meva: ", mevalar[1].upper())

car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen','Damas']
print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 


narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
print(narhlar)


mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
mevalar.append(narhlar)
mevalar.insert(1, "Gilos")
print(mevalar)

del mevalar[3]
print(mevalar)

mevalar.remove("o'rik")
print(mevalar)

new_arr = mevalar.pop(-1)
print(new_arr[1])




