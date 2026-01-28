while True:
    try:
        n = input("Enter year: or enter 'q' for quit! ").strip()
        if n.lower() == 'q':
            break
        n = int(n)

        if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
            print("This is Leap Year:", n)
        else:
            print("This isn't Leap Year:", n)

    except ValueError:
        print("Invalid input!")
