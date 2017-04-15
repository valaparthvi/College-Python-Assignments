num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
try:
    division = num1 // num2
    print("%d / %d = %d" % (num1, num2, division))
except ZeroDivisionError as e:
    print("Sorry! Cannot divide by 0.")

'''
Output: python3 chapter4_4_zerodivisionerror.py
Enter number1: 19
Enter number2: 0
Sorry! Cannot divide by 0.
'''
