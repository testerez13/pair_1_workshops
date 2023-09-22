#************************************ CEVAP-1 *****************************

# def calculater(num1,num2):
#     print("1- Toplama\n2- Çıkarma\n3- Çarpma\n4- Bölme")
#     userChose = int(input("Lütfen seçeneklerden birini tercih ediniz: "))


#     if userChose==1:
#         print(num1+num2)
#     elif userChose==2:
#         print(num1-num2)
#     elif userChose==3:
#         print(num1*num2)
#     elif userChose==4:
#         print(num1/num2)
#     else:
#         print("Hatalı giriş yaptınız!")

# number1 = int(input("Lütfen hesap maiknesi için 1. sayıyı giriniz: "))
# number2 = int(input("Lütfen hesap maiknesi için 2. sayıyı giriniz: "))

# calculater(number1,number2)




#************************************ CEVAP-2 *****************************

# def somesterAvarage(final,vize):
    
#     avarage =vize*0.4+final*0.6
#     if avarage>=0 and avarage<=49:
#         print(f"{avarage} - FF")
#     elif avarage>=50 and avarage<=59:
#         print(f"{avarage} - DD")
#     elif avarage>=60 and avarage<=69:
#         print(f"{avarage} - CC")
#     elif avarage>=70 and avarage<=79:
#         print(f"{avarage} - BB")
#     elif avarage>=80 and avarage<=100:
#         print(f"{avarage} - AA")
#     else:
#         print("Lütfen tekrar deneyin ve geçerli değerler giriniz!")

# final= int(input("Lütfen final notunu giriniz: "))
# vize = int(input("Lütfen vize notunu giriniz: "))

# somesterAvarage(final,vize)



#************************************ CEVAP-3 *****************************


# def fullNameArray():
#     fullName=[]
#     for i in range(10):
#         fullName.append(input(f"{i+1}. Ad Soyadı giriniz: "))
    
#     print(fullName)

# fullNameArray()


#************************************ CEVAP-4 *****************************


# fibonacciArray =[1,1]

# for f in range(18):
#     fibonacciArray.append(fibonacciArray[-1]+fibonacciArray[-2])

# print(fibonacciArray)


#************************************ CEVAP-5 *****************************


# def perfectNumber(userNumber) -> str:
#     sumofindex=0
#     for i in range(1,userNumber):
#         if userNumber % i==0:
#             sumofindex =sumofindex+i

#     if userNumber ==sumofindex:
#         return f"Mükemmel Sayı - {userNumber}"
#     else:
#         return f"Mükemmel Sayı değil - {userNumber}"


# userNumber = int(input("Lütfen sayı giriniz: "))
# print(perfectNumber(userNumber))