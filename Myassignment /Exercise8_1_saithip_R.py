username = input("Enter your username: ")
password = input("Enter your password: ")

if username != "arttoyshop" or password != "987456":
    print("Apologize, your username and password probably wrong!!")
else:
    print(f"Hello, {username}, may I help you?")
    
    crybaby_price = 500
    molly_price = 450
    hirono_price = 400
    labubu_price = 500

    while True:
        print("Your Welcome!! to arttoyshop")
        print("==============================")
        print("         Product List         ")
        print(f"1.) crybaby = {crybaby_price} THB")
        print(f"2.) molly = {molly_price} THB")
        print(f"3.) hirono = {hirono_price} THB")
        print(f"4.) labubu = {labubu_price} THB")
        print("==============================")

        product = int(input("Select Order number >> "))

        if product == 1:
            quantity = int(input("Quantity: "))
            total = crybaby_price * quantity
            print(f"Total Price is: {total} THB")

        elif product == 2:
            quantity = int(input("Quantity: "))
            total = molly_price * quantity
            print(f"Total Price is: {total} THB")

        elif product == 3:
            quantity = int(input("Quantity: "))
            total = hirono_price * quantity
            print(f"Total Price is: {total} THB")

        elif product == 4:
            quantity = int(input("Quantity: "))
            total = labubu_price * quantity
            print(f"Total Price is: {total} THB")

        else:
            print("Apologize, your required number doesn't exist.")
        
        print("Back to menu? (yes or no)")
        decide = input("Pick choice: ").lower()
        if decide != "yes":
            print("Sign-out from system automate")
            break

    print("Thank you for buying")
