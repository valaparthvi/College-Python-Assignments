try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise(ValueError)
    else:
        print("Oh, so you're %d years old! That's great!" % age)
except ValueError as e:
    print("Please enter a valid age which is a positive integer.")

'''
Output: python3 chapter4_5_agevalidator.py

Enter your age: 14
Oh, so you're 14 years old! That's great!
'''
