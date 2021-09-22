
def main():
    s = input("Please enter a list of integers: ")
    lst = s.split()
    newlst = []
    for i in lst:
        if int(i) % 2 == 0:
            newlst.append(int(i))
            print(i, end=" ")
    print()
    print(newlst)


if __name__ == "__main__":
    main()
