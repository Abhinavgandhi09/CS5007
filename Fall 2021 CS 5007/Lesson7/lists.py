

def numberOfNegative(listOfLists):
    count = 0
    for i in range(len(listOfLists)):
        for j in range(len(i)):
            if i[j] < 0:
                count += 1

    return count



def main():
    my_list = [[-1,2,3,-4],[1,4],[2,-5,6,7],[2,3,4,-1]]
    print(numberOfNegative(my_list))


if __name__ == "__main__":
    main()