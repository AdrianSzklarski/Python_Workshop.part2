print("Quadrature equation a*x**2 + b*x + c == 0")
var_a = int(input("Enter value a: "))
var_b = int(input("Enter value b: "))
var_c = int(input("Enter value c: "))
delta = (var_b ** 2) - (4 * var_a * var_c)
print(delta)
if delta > 0:
    x1 = (-var_b - (delta ** 0.5)) / (2 * var_a)
    x2 = (-var_b + (delta ** 0.5)) / (2 * var_a)
    print("Roots of quadratic equation: ")
    print("x1 = ", x1)
    print("x2 = ", x2)
elif delta == 0:
    x3 = -var_b / (2 * var_a)
    print("Roots of quadratic equation: ")
    print("x1 = x2 = ", x3)
else:
    print("No solutions in the field of numbers R")
    delta_i = abs(delta)  # i = -1
    print("Solution in the domain of complex numbers  Z")
    print("x1 = ", -round(var_b / (2 * var_a),3), "-", round((delta_i ** 0.5) / (2 * var_a),3), "i")
    print("x2 = ", -round(var_b / (2 * var_a),3), "+", round((delta_i ** 0.5) / (2 * var_a),3), "i")
