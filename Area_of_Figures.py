tupe = input()
from math import pi
if tupe == 'square':
    a = float(input())
    square = a * a
    print(f"{square:.3f}")
elif tupe == 'rectangle':
    a = float(input())
    b = float(input())
    rectangle = a * b
    print(f"{rectangle:.3f}")
elif tupe == "circle":
    a = float(input())
    circle = pi * (a ** 2)
    print(f"{circle:.3f}")
elif tupe == "triangle":
    a = float(input())
    b = float(input())
    triangle = a * b / 2
    print(f"{triangle:.3f}")
