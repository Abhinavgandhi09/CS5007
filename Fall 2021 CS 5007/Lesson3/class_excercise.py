# Formatting the output by specifying the number of decimal places to display
import math


def main():
    outer_r = float(input("Enter the radius of the outer circle: "))
    inner_r = float(input("Enter the radius of the inner circle: "))
    outer_area = math.pi * outer_r ** 2
    inner_area = math.pi * inner_r ** 2
    answer = outer_area - inner_area
    print()
    print("The area of the part between the inner circle and outer circle is: ", answer)
    print("The area of the part between the inner circle and outer circle is: ", "%1.4f" % answer)
    print("The area of the part between the inner circle and outer circle is: ", round(answer, 4))

if __name__ == "__main__":
    main()

