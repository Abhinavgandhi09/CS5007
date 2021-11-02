def rec_factorial(n):
    if n == 0:
        return 1
    else:
        return rec_factorial(n-1) * n


def base_factorial(n):
    fact = 1
    if n == 0:
        return 1
    else:
        for i in range(n):
            fact *= n
            n = n - 1
        return fact

def main():
    n = int(input("Enter number: "))
    print(base_factorial(n))
    print(rec_factorial(n))


if __name__ == "__main__":
    main()

