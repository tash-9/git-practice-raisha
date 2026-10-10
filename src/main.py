from datetime import date
from utils import add, subtract,multiply,divide

print("My name is Tasfia Islam Raisha")
print("Date Today: ", date.today())

print("Addition of 2 and 2:", add(2, 2))
print("Subtraction of 5 from 10", subtract(10, 5))
print("Multiplication 6 and 6:", multiply(6, 6))

print("Division of 144 by 12:", divide(144, 12))

try:
    print("Division of 144 by 0:", divide(144, 0))
except ValueError as error:
    print("Division of 144 by 0 (Error): ", error)