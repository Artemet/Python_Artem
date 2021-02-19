anser = input("зарегистрироваться?: ")
if anser == "да":
    name = input("Name: ")
    parol = input("Parol: ")
    regestName = {"name": name}
    regestParol = {"parol": parol}
    command = input("command: ")
    if command == "start":
        i = 0
        for i in command:
            productStart = input("product: ")
            arrProduct = [productStart]
            print(arrProduct)
            productTwo = input("product: ")
            arrProduct = [productStart, productTwo]
            print(arrProduct)
            productThree = input("product: ")
            arrProduct = [productStart, productTwo, productThree]
            print(arrProduct)
            productFour = input("product: ")
            arrProduct = [productStart, productTwo, productThree, productFour]
            print(arrProduct)
            productFive = input("product: ")
            arrProduct = [productStart, productTwo, productThree, productFour, productFive]
            print(arrProduct)
            productSix = input("product: ")
            arrProduct = [productStart, productTwo, productThree, productFour, productFive, productSix]
            print(arrProduct)
            productSeven = input("product: ")
            arrProduct = [productStart, productTwo, productThree, productFour, productFive, productSix, productSeven]
            print(arrProduct)
            productEight = input("product: ")
            arrProduct = [productStart, productTwo, productThree, productFour, productFive, productSix, productSeven, productEight]
            print(arrProduct)
            productNine = input("product: ")
            arrProduct = [productStart, productTwo, productThree, productFour, productFive, productSix, productSeven, productEight, productNine]
            print(arrProduct)
            productTen = input("product: ")
            arrProduct = [productStart, productTwo, productThree, productFour, productFive, productSix, productSeven, productEight, productNine, productTen]
            print(arrProduct)
            peaoleAnser = input("Delit?: ")
            if peaoleAnser == "yes":
                delitProduct = input("which?: ")
                if delitProduct == arrProduct[0]:
                    arrProduct.pop(0)
                    print(arrProduct)
                elif delitProduct == arrProduct[1]:
                    arrProduct.pop(1)
                    print(arrProduct)
                elif delitProduct == arrProduct[2]:
                    print(arrProduct)
                elif delitProduct == arrProduct[3]:
                    print(arrProduct)
                elif delitProduct == arrProduct[4]:
                    print(arrProduct)
                elif delitProduct == arrProduct[5]:
                    print(arrProduct)
                elif delitProduct == arrProduct[6]:
                    print(arrProduct)
                elif delitProduct == arrProduct[7]:
                    print(arrProduct)
                elif delitProduct == arrProduct[8]:
                    print(arrProduct)
                elif delitProduct == arrProduct[9]:
                    print(arrProduct)
            elif peaoleAnser == "no":
                print(name,"bye!")
            close = input("finish?: ")
            if close == "yes":
                print(name, "bye!")
                break
            peaoleAnserDelit = input("more: ")
    elif command == "show":
        file = open("show.txt", "w")
        file.write("Name: ")
        file.write(name)
        file.write(" Parol: ")
        file.write(parol)
        file.close()
    elif command == "none":
        print(name,"bye!")
elif anser == "no":
    print("bye!")
else:
    print("Problem!")