def writeVertical(n):
    if 0 <= n < 10:
        print(n)
    elif n < 0:
        print("-")
        writeVertical(-n)
    else:
        writeVertical(n//10)
        print(n%10)


def negdisp(n):
    if len(n) == 1:
        print(n)
    else:
        negdisp(n[0:len(n)-1])
        print(n[-1])


def disp(n):
    if n < 10:
        print(n)
    else:
        disp(n//10)
        print(n % 10)


def main():
    n = int(input("Enter number: "))
    # print(disp(n))

    # print(negdisp(str(n)))
    print(writeVertical(n))


if __name__ == "__main__":
    main()