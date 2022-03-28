
def area(m, n):
    r1 = m * n
    return r1


def perimeter(m, n):
    r2 = 2 * (m + n)
    return r2


def square(g):
    r3 = g * g
    return r3


if __name__ == "__main__":
    f = 1

    while f:
        print("menu :")
        print("1. area of rectangle  ")
        print("2. perimeter of rectangle ")
        print("3. area of square ")
        print("4. exit ")
        a = int(input("enter ur selection : "))





        if a == 1:
            le = float(input("enter length : "))
            b = float(input("enter breadth : "))
            print(area(le, b))

        if a == 2:
            le = float(input("enter length : "))
            b = float(input("enter breadth : "))
            print(perimeter(le, b))

        if a == 3:
            h = float(input("enter length of one side of square : "))
            print(square(h))

        if a == 4:
            f = 0