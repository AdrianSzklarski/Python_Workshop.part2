"""     Adrian SZKLARSKI, 12.2021r,
          Quadrature Equation:

Program calculates quadratic equation for Delta:

    Returns:    Delta > 0; Delta = 0; Delta < 0.

    Parameters: Enter value for Quadrature
                equation a*x**2 + b*x + c == 0

    Error:     except ValueError or NameError:
               You should have given either an int or a float

"""


def Quadrature_equation(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    print('Delta = ', delta)

    if delta > 0:
        if a == 0:
            x1 = round((-b - (delta ** 0.5)), 3)
            x2 = round((-b + (delta ** 0.5)), 3)
        else:
            x1 = round((-b - (delta ** 0.5)) / (2 * a), 3)
            x2 = round((-b + (delta ** 0.5)) / (2 * a), 3)
        print("Roots of quadratic equation are: ")
        print("x1 = ", x1)
        print("x2 = ", x2)
    elif delta == 0:
        x3 = -b / (2 * a)
        print("Roots of quadratic equation: ")
        print("x1 = x2 = ", x3)
    else:
        print("No solutions in the field of numbers R")
        print("Solution in the domain of complex numbers  Z")
        delta_i = abs(delta)  # i = -1
        print("x1 = ", -round(b / (2 * a), 3), "-", round((delta_i ** 0.5) / (2 * a), 3), "i")
        print("x2 = ", -round(b / (2 * a), 3), "+", round((delta_i ** 0.5) / (2 * a), 3), "i")


if __name__ == '__main__':
    while True:
        print("Quadrature equation a*x**2 + b*x + c == 0")
        try:
            a = float(input("Enter value a: "))
            b = float(input("Enter value b: "))
            c = float(input("Enter value c: "))
            print(' ')
            break
        except ValueError or NameError:
            print("You should have given either an int or a float")
            print(' ')

result = (Quadrature_equation(a, b, c))

