def linear_sum(A, n):
    if n == 0:
        return 0
    elif n == 1:
        return A[0]
    else:
        return linear_sum(A, n-1) + A[n-1]


def list_sum(a):
    if len(a) == 0:
        return 0
    elif len(a) == 1:
        return a[0]
    else:
        return list_sum(a[1:]) + a[0]


def main():
    n = int(input("Enter length: "))
    a = []
    for i in range(n):
        a.append(int(input("Enter element: ")))

    # print(list_sum(a))
    print(linear_sum(a, n))

if __name__ == "__main__":
    main()