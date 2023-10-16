from datetime import date

year = date.today().year

avtolar = ['audi','bmw','volvo','kia','hyundai']

for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
    if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
        print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
    else: # aks holda ... 
        print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.

ism = "Abdulbosit"

if ism.lower() == "abdulbosit":
    print(True)
else:
    print(False)


ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
else:
    print("Salom, ", ism)

javob = float(input("12x6 nechiga teng?>>>"))
if javob!=72:
    print("Javob xato!")
else:
    print('Congratulation!')

yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>=18: # yosh 18 dan katta yoki teng bo'lsa
    print('Xush kelibsiz!')
else: # ask holda
    print('Kirish mumkin emas!')

login = input("Yangi login tanlang:")
if len(login)<=5: # login uzunligini tekshiramiz
    print("Login 5 harfdan ko'proq bo'lishi shart!")
    login = input("Qayta kiriting: ")
else:
    print("Saved")


yil = int(input("Tug'ilgan yilingizni kiriting:"))
if year-yil<18: # foydalanuvchining yoshini hisoblaymiz
    print(f"Yoshingiz {year-yil} da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!")


#amaliyot
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

for car in cars:
    if car.upper()=="GM":
        print(car.upper())
    else:
        print(car.title())