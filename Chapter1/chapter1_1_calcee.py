op = input("Select an operator from [+, -, /, *]\n")
op_lst = ['+', '-', '*', '/']

while op not in op_lst:
    op = input(
        "You did not enter correct operator \nPlease select from [+, -, /, *]\n")

num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))

if op == '+':
    print("%d + %d = %d" % (num1, num2, num1 + num2))
if op == '-':
    print("%d - %d = %d" % (num1, num2, num1 - num2))
if op == '*':
    print("%d * %d = %d" % (num1, num2, num1 * num2))
if op == '/':
    print("%f * %f = %f" % (num1, num2, num1 / num2))


'''
Ouput: python3 chapter1_1_calcee.py

Select an operator from [+, -, /, *]
&
You did not enter correct operator
Please select from [+, -, /, *]
-
Enter number1: 14
Enter number2: 15
14 - 15 = -1
'''
