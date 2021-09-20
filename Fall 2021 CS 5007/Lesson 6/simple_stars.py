

def simple_stars(n):
    res = ""
    for i in range(1, n+1, 1):
        for j in range(i):
            res = res + "* "
            # print("*", end = "")
        # print()
        res = res + "\n" +"\n"
    print(res)


def main():
    n = int(input("Please enter an integer: "))
    if n < 1:
        n = int(input("Please enter an integer > 1: "))
    simple_stars(n)



if __name__ == "__main__":
    main()