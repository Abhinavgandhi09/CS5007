
def main():

    n1 = 5
    n2 = 2
    n3 = 5.5
    n4 = str(n3)
    i = 1

    print(str(n1)+" + "+str(n2)+" = "+str(n1+n2))
    print(str(n1) + " - " + str(n2) + " = " + str(n1 - n2))
    print(str(n1) + " * " + str(n2) + " = " + str(n1 * n2))
    print(str(n1) + " / " + str(n2) + " = " + str(n1 / n2))
    print(str(n1) + " // " + str(n2) + " = " + str(n1 // n2))
    print(str(n1) + " ** " + str(n2) + " = " + str(n1 ** n2))
    print(str(n1) + " % " + str(n2) + " = " + str(n1 % n2))
    print("abs("+str(-n1)+")"+" = "+str(abs(-n1)))
    print("int("+str(n3)+")"+" = "+str(int(n3)))
    print("float(\""+n4+"\")"+" = "+str(float(n4)))
    print("complex("+str(n1)+","+str(i)+")"+" = "+str(complex(n1,i)))



if __name__ == "__main__":

    main()