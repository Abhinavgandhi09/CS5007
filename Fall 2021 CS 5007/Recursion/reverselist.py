reverse_ls = []
main_ls = []


def rev_ls(ls):
    global reverse_ls
    if len(ls) == 1:
        reverse_ls.append(ls[0])
        return reverse_ls
    else:
        reverse_ls.append(ls[-1])
        return rev_ls(ls[0:-2])


def main():
    global main_ls
    size = int(input("Enter list size: "))

    for i in range(size):
        main_ls.append(input("Enter list element: "))

    print(rev_ls(main_ls))


if __name__ == "__main__":
    main()