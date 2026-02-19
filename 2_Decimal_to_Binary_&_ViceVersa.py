# Decimal to Binary
def dec_to_bin(num):

    if num <= 0:
        print("Only positive numbers supported")
        return
    
    number = int(num)
    ans = []

    while number > 0:
        remainder = number % 2
        ans.append(str(remainder))
        number //= 2   # integer division

    ans.reverse()
    print(f"Decimal {num} | Binary {''.join(ans)}")
    print()
    
# Binary to Decimal
def bin_to_dec(num):
    number = 1
    result = [int(digit) for digit in str(num)]
    results = result[::-1]
    ans = int()
    for i in (results):
        ans = ans + (i*number)
        number = number * 2
    print()
    print(f"Binary {num} | Decimal {ans}")
    print()


def start():
    while True:
        try:
            user_input = input("'1' Decimal Number to Binary Number\n'2' Binary Number to Decimal Number\n'3' to Exit\n:")
            user_input = int(user_input)
            if user_input in range(4):
                #  1 Dec to Bin
                if user_input == 1:
                    print("Decimal Number to Binary Number")
                    while True:
                        try:
                            num = input("Enter any Number or press 'q' for back... ")
                            if num.lower()=='q':
                                print("...")
                                break

                            num = int(num)

                            if num == 0:
                                print(f"Decimal 0 | Binary 0")
                            elif num == 1:
                                print(f"Decimal 1 | Binary 1")
                            else:
                                #print()
                                #print("Binary: {}".format(bin(num)[2:])) # Automatically
                                dec_to_bin(num)
                        except ValueError:
                                print("Invalid Decimal Number!")
                #  2 Bin to Dec
                elif user_input == 2:
                    print("Binary Number to Decimal Numbe")
                    while True:
                        try:
                            num = input("Enter any Number or press 'q' for back... ")
                            if num.lower()=='q':
                                print("...")
                                break

                            if num.startswith("-"):
                                print("Invalid (positive numbers only)")
                                continue

                            if num == 0:
                                print(f"Binary 0 | Decimal 0")
                            elif num == 1:
                                print(f"Binary 1 | Decimal 1")
                            elif any(d not in '01' for d in num):
                                raise Exception()
                            else:
                                #print()
                                #print("Decimal: {}".format(int(num, 2))) # Automatically
                                bin_to_dec(num)
                        except:
                            print("Invalid Binary Number!")
                #  3 Exit
                else:
                    print(".....")
                    break
            else:
                print("Invalid Choice!") 
                continue
        except:
                print("Invalid input!")

print("Welcome...\nThis program supports positive numbers only.")

start()
