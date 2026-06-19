while True:
    try:
        I=int(input("Enter a number between 1 to 10:"))
    except ValueError:
        print("Please enter a number")
        continue
    if 1<=I<=10:
        print(f"Great!You entered {I}")
        break
    else:
        print("Please enter a number between 1 to 10")
