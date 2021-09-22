def main():
    s = input("Please enter a list of integers: ")
    lst = s.split()
    count = 0
    # print(lst)
    for e in lst:
        count = count + 1

    print("There were ", count, "integers in the list")


if __name__ == "__main__":
    main()



