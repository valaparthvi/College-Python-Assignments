gender = input(
    "Enter M if you are Male.\nEnter F if you are Female.\n").upper()
current_salary = int(input("Enter your current salary: "))

if current_salary < 1000 and gender == 'M':
    current_salary += ((current_salary * 5) / 100)

elif current_salary < 1000 and gender == 'F':
    current_salary += ((current_salary * 5.5) / 100)

else:
    current_salary += ((current_salary * 5) / 100)

print("Your new salary is %f" % current_salary)


'''
Output: python3 chapter1_2_bonus.py

Enter M if you are Male.
Enter F if you are Female.
m
Enter your current salary: 500
Your new salary is 525.000000
'''
