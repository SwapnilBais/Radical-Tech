Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> #MyCalculator#SwapnilBais@Bunny
def add():
    return float(input ("Enter the first number: ")) + float(input ("Enter the second number: "))

def sub():
    return float(input ("Enter the first number: ")) - float(input ("Enter the second number: "))

def mul():
    return float(input ("Enter the first number: ")) * float(input ("Enter the second number: "))

def div():
    return float (input ("Enter the first number: ")) / float (input ("Enter the second number: "))

def power():
    return float(input ("Enter the first number: ")) ** float(input ("Enter the second number: "))

s = input("Add, Sub, Mul, Div or Power of two Numbers: ")
if s == "add":
    print(add ())
elif s == "subtract":
    print(sub ())
elif s == "multiply":
    print(mult ())
elif s == "power":
    print(power ())
elif s == "division":
    print(division ())
else:
    print ("Enter a valid option")
    
