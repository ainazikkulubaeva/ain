while True:
    print( "Калькулятор" )
    a = float(input("Биринчи санды киргизиниз: "))
    b = float(input("Экинчи санды киргизиниз: "))

    print("1.Кошуу(+)")
    print("2.Кемитүү(-)")
    print("3.Көбөйтүү(*)")
    print("4.Болүү(:)")

    choice = input("Oпперацияны танданыз(1-4): ")

    if choice =="1":
        print("Жооп:", a+b)
    elif choice == "2":
        print("Жооп:", a-b)
    elif choice == "3":
        print("Жооп:", a*b)
    elif choice =="4":
        if b !=0:
            print("Жооп:", a/b)
        else:
            print("Kaта! 0гө бөлүүгө болбойт.")
    else:
            print("Туура эмес тандоо!")
    answer = input("Дагы эсептейсизби? (Ооба/Жок):").lower()
    if answer== "Жок":
        print("Программа аяктады! :) ")
    break