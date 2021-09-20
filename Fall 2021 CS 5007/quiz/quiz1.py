def main():
    n1 = float(input("Enter the 1st Number: "))
    n2 = float(input("Enter the 2nd Number: "))
    print()

    while (n1 != 0) or (n2 != 0):
        _sum = n1 + n2
        prod = n1 * n2
        avg = (n1 + n2) / 2

        if _sum > 200:
            print("SUM = ", round(_sum, 1), " *")
        else:
            print("SUM = ", round(_sum, 1))

        print("PRODUCT = ", round(prod, 1))
        print("AVERAGE = ", round(avg, 1))
        print()

        n1 = float(input("Enter the 1st Number: "))
        n2 = float(input("Enter the 2nd Number: "))
        print()

    print("Both numbers are zero!")


if __name__ == "__main__":
    main()
