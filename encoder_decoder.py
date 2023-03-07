def encode(string):
    newstring = ''
    for x in string:
        newstring += str((int(x) + 3) % 10)
    return newstring

def decode(string):
    pass

def main():
    pw = None
    while True:
        print("Menu:")
        print("------------- ")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        awp = int(input("Please enter an option:"))
        if awp == 1:
            passw = input("Please enter a password to encode:")
            pw = passw
            print("Your password has been stored and encoded!")
        elif awp == 2:
            print(f"Your encoded password is {encode(pw)}, and the original password is {pw}")
        elif awp == 3:
            break


if __name__ == "__main__":
    main()
