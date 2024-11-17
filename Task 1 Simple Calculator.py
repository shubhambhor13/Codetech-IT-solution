# TASK ONE: SIMPLE CALCULATOR
num1 = float(input("Enter a first number"))
oper = (input("enter a operator (+,-,*,/,%)"))
num2 = float(input("Enter a second number"))

if oper == "+":
    print(num1+num2)   
elif oper == "-":
    print(num1-num2)
elif oper == "*":
    print(num1*num2)
elif oper == "/":
    if num2!=0:
        print(num1/num2)
    else:
        print("zero is not allowed")
elif oper == "%":
    print(num1/num2*100)
else:
    print("enter a wrong operator")
