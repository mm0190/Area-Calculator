import math

def calculate_square_area(side):
    return side ** 2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return (base * height) / 2

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def main():
    print("==================")
    print("Area Calculator 📐")
    print("==================")
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit")

    choice = input("\nWhich shape: ")

    if choice == '1':
        base = float(input("Base: "))
        height = float(input("Height: "))
        area = calculate_triangle_area(base, height)
        print("\nThe area is", area)
    elif choice == '2':
        length = float(input("Length: "))
        width = float(input("Width: "))
        area = calculate_rectangle_area(length, width)
        print("\nThe area is", area)
    elif choice == '3':
        side = float(input("Side: "))
        area = calculate_square_area(side)
        print("\nThe area is", area)
    elif choice == '4':
        radius = float(input("Radius: "))
        area = calculate_circle_area(radius)
        print("\nThe area is", area)
    elif choice == '5':
        print("\nExiting program...")
    else:
        print("\nInvalid choice. Please select a number from 1 to 5.")

if __name__ == "__main__":
    main()
