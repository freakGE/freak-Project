def web_momxmarebeli():
    print('Mogesalmebit!')
    print('Ketili iyos tqveni mobrdzaneba')
    update = input("Programas schirdeba ganaxleba, winaamdegi homarxart, rom ganvaaxlot?: ")
    if update == "ara":
        print("-----" * 16)
        print("Ganaxlda")
        account = input("Gindat sheqmnat tqveni akaunti?: ")
        if account == "kargi" or "ki" or "diax":
            account_firstname = input("Saxeli: ")
            account_lastname = input("Gvari: ")
            genders = input("1. Qali\n2. Kaci\nGender: ")
            if genders == "2":
                gender = "Batono"
            elif genders == "1":
                gender = "Qalbatono"
            else:
                gender = "Transeqsualo"
            mail = input("Mail: ")
            password = input("Password: ")
            print(f"{gender} {account_firstname} tqveni akaunti warmatebit sheiqmna")
            print("-----" * 64)
        else:
            print("Kargit tqven gaqvt shezguduli uflebebi radgan argaqvt akaunti")
            print(".*." * 64)
    else:
        print("Programa shezgudulia radgan ar ganaxlebula")

    
    account_mail = input("Gtxovt sheiyvanot maili\nMail: ")
    if account_mail == mail:
        account_password = input("Gtxovt Sheiyvanot paroli \nPassword: ")
        if account_password == password:
            print(f"{gender} {account_firstname} ketili iyos tqveni mobrdzaneba")
        else:
            print("Tqven shecdomit sheiyvanet mail an paroli")
    else:
        print("Tqven shecdomit sheiyvanet mail an paroli")
        
        
web_momxmarebeli()


    


