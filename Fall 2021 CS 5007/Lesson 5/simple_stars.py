

def main():
    n = int(input("Please enter an integer: "))
    if n < 1:
        n = int(input("Please enter an integer > 1: "))

    for i in range(1,n+1,1):
        for j in range(i):
            print("*", end = "")
        print()


if __name__ == "__main__":
    main()