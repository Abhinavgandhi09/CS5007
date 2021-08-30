# Input function always returns string
# We can convert this string into whatever class we want

def main():
    base = float(input("Enter a number: "))
    exp = float(input("Enter an exponent: "))
    answer = base ** exp
    print(str(base)+"^"+str(exp),"=",answer)

if __name__ == "__main__":
    main()
