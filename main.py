while True:
    students = ["recep tayyip","kemal kılıçdaroğlu","muharrem ince"]
    
    accountValue = input("yapmak istediğiniz işlemi seçiniz.Eğer Öğrenci Eklemek istiyorsanız 1 i silmek istiyorsanız 2 yi tüm öğrencileri görmek için 3 ü girin : ")
    if accountValue == "1":
        def studentAdd():
            studentName = input("öğrencinin adını giriniz")
            # studentSurname = input("öğrencinin soy adını giriniz")
            # nameAndSurname = studentName + " "+ studentSurname
            print(studentName)
            students.append(studentName)
            print(students)
        studentAdd()    
    elif accountValue == "2":
        def studentDelete():
            studentName = input("öğrencinin adını giriniz")
            # studentSurname = input("öğrencinin soy adını giriniz")
            # nameAndSurname = studentName + " "+ studentSurname
            print( studentName)
            for i in students:
                if i ==  studentName:
                    students.remove(i)
                    print("elaman silindi")
                    break; 
        studentDelete()
    elif accountValue =="3":
        def writeToAllStudent():
            for i in students:
                print(i)  
        writeToAllStudent()
    elif accountValue =="4":
        def learningNumber():
         studentName = input("öğrencinin adını giriniz")  
         print(students.index(studentName))
        learningNumber() 

    else:
        print("yanlış değer girdiniz")


                          
            