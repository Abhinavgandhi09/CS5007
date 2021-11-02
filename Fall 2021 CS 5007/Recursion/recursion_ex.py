def sumFirstN(n):

    if n == 0:
        return 0
    else:
        return sumFirstN(n-1) + n


def main():
    n = int(input("Enter a non-negative integer: "))
    s = sumFirstN(n)

    print(s)


if __name__ == "__main__":
    main()
