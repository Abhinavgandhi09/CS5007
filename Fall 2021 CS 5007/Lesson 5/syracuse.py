

def main():
    n = int(input("Please enter an integer >= 1: "))
    print(n, end = " ")
    while n > 1:
        if n%2 == 0:
            n = n/2
        else:
            n = n*3 + 1
        print(int(n), end = " ")


if __name__ == "__main__":
    main()
