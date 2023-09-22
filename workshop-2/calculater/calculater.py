#Versiondan dolayı switch case yapısı yerine if-else kullanılarak yazıldı.

#*************************** CEVAP-1 ****************************


class Calculater:
    num1=0
    num2=0

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def addition(self) -> float:
        return (int(self.num1) + int(self.num2))
    
    def subtraction(self) -> float:
        return (int(self.num1) - int(self.num2))

    def multiplication(self) -> float:
        return (int(self.num1) * int(self.num2))
    
    def division(self) -> float:
        return (int(self.num1) / int(self.num2))
    
    def mod(self) -> float:
        return (int(self.num1) % int(self.num2))    

while True:
    print("(+) Toplama\n(-) Çıkarma\n(*) Çarpma\n(/) Bölme\n(%) Mod\n(q) Çıkış")
    userChose = input("Yapmak istediğiniz işlemi seçiniz: ")
    if userChose=="q":
        print("Çıkış işlemi başarıyla gerçekleşmiştir.")
        break
    elif userChose not in ('+', '-', '*', '/', '%'):
            print("Yanlış seçim yaptınız. Lütfen daha sonra tekrar deneyiniz.")
            break
    else:
        number1 = input("Lütfen ilk sayıyı giriniz: ")
        number2 = input("Lütfen ikinci sayıyı giriniz: ")

        calculater1 = Calculater(number1,number2)

        if userChose=="+":
            print(calculater1.addition())
        if userChose=="-":
            print(calculater1.subtraction())
        if userChose=="*":
            print(calculater1.multiplication())
        if userChose=="/":
            print(calculater1.division())
        if userChose=="%":
            print(calculater1.mod())


