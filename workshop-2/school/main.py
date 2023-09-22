from student import Student
from teacher import Teacher
list =[]

def add(type, obj):

    if type == 1:
        st1 =Student()
        st1=obj
        list.append([st1.fullname,st1.age])
    else:
        tc1 = Teacher()
        tc1=obj
        list.append([tc1.profession,tc1.sex])

    
def writer():
    print("\n *************************************** BİLGİLER ***************************************\n")
    for l in list:
        print(l)

while True:

    print("\n *************************************** KAYIT ***************************************\n")
    userChose= int(input("1- Öğrenci Kaydı \n2- Öğrentmen Kaydı\n3- Yazdır\n4- Çıkış\n"))
    if userChose == 4:
        print("Çıkış başarıyla gerçekleşmiştir")
        break
    elif userChose not in (1,2,3):
            print("Hatalı giriş yaptınız!")
    elif userChose ==1:
        student1 = Student()
        student1.fullname=input("Öğrenci adı gir: ")
        student1.age=input("Öğrenci yaşı gir: ")
        student1.isStudent=1
        add(1,student1)
    elif userChose ==2:
        teacher1 = Teacher()
        teacher1.profession = input("Öğretmen bölümü gir: ")
        teacher1.sex = input("Öğretmen cinsiyeti gir: ")
        teacher1.isStudent=2
        add(2,teacher1)
    else:
        writer()


        

    










# makeList()

