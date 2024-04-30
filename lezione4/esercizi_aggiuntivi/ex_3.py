def product_def(name, price, quantity):
    product : dict = {
        "Name": name,
        "Price": price,
        "Quantity": quantity
    }
    return product

def shopping_cart():                    #UTILIZZA LE LISTE, DA SISTEMARE CON I DIZIONARI (https://python-forum.io/thread-37566.html)
    cart  =[]
    prices = []
    total = []
    total_price = []
    while True :
        print()
        print("Please type in one of these: ")

        print("1. Add item\n2. Remove Item\n3. View Products\n4. Cart Amount")
        
        input_choise = int(input("Select a number to go on: "))

        item = ""

        if input_choise == 1 :                                                          #SCELTA 1
            while item != "ok":
                item = input("Write the name of the pruduct: ")
                price = int(input("Type in the price: "))
                prices.append(price)

                ok = input("Type ok for coming back to the start menu ")
                if item != "ok":
                    cart.append(item)
                    print(f"{item} has been added")
                    print(f"The price is {price}")
                    break

        elif input_choise == 2 :                                                          #SCELTA 2
            print("This is your cart: {}".format(cart))
            takeout = input("Type in what do you want to remove: ")
            cart.remove(takeout)
            continue
                

        elif input_choise == 3 :                                                            #SCELTA 3
            print("This is what is in your shopping cart: ")
            for item in cart:
                print(item, price)
                break
        

        #elif input_choise == 4 :                                                            #SCELTA 4

    
shopping_cart()