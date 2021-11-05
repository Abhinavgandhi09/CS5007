import math


def binarySum(A, i, n):
    if n == 0:
        return A
    elif n == 1:
        return A[i]
    else:
        binarySum(A, i, math.ceil(n/2)) + binarySum(A, i + math.ceil(n/2), math.floor(n/2))


def main():

    x = (input("Enter list: "))
    ls = x.split()

    print(binarySum(ls, 0, len(ls)))


if __name__ == "__main__":
    main()