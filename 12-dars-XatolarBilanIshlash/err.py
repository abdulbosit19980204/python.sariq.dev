#print "Hello World!"

#Natija: SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello World!")?


print("Hello World!

#Natija: SyntaxError: EOL while scanning string literal

print("Hello World!"
# Natija: SyntaxError: unexpected EOF while parsing
# EOF xatoligining muammoli tarafi, Python aynan qaysi funktsiya yopilmay qolganini ko'rsata olmaydi, ya'ni kodni sinchiklab ko'zdan kechirib chiqish talab qilinad


# IndentationError - JOY TASHLASHDA XATOLIK
print("O'ngacha sanaymiz")
for n in range(10):
print(n+1)

# RUN TIME ERROR - DASTURNI BAJARISHDA XATOLIK
# Run time error — dastur bajarish jarayonida kelib chiqadi va dasturning ishlashini to'xtatadi. Sintaks xatolikdan farqli ravishda Python bunday xatolarni dasturni bajarishdan avval aniqlay olmaydi. Run time error ning bir necha turi bor. Keling, ulardan ba'zilari bilan tanishamiz.

# TypeError
# Biror amalni (funktsiya, metod) noto'g'ri ma'lumot turi ustida bajarish. 
son = input("Istalgan son kiriting: ")
print(f"{son} ning kvadrati {son**2} ga teng")

# NameError

# O'zgaruvchi, funktsiya, obyekt nomini noto'g'ri yozish natijasida kelib chiquvchi xatolik
prit("Hello World!")
# Natija: NameError: name 'prit' is not defined

mevalar = ['olma','uzum','nok','anor','anjir']
for meva in mvealar:
    print(meva)

# Natija: NameError: name 'mvealar' is not defined