def main():
    income = float(input("Please enter your net annual income: "))
    if income <= 15000:
        print("Tax due: $0.00")
    elif income <= 30000:
        print("$" + str(income - 15000) + " taxed @ 5%, tax due: $" + str(0.05*(income - 15000)))
    else:
        print("$15000 taxed @ 5% + $" + str(income - 30000) + " taxed @ 10%, tax due: $" + str(0.05*15000 + 0.1*(income - 30000)))


if __name__ == "__main__":
    main()

