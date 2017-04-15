try:
    score = float(input("Enter your score: "))
    while not(0.0 <= score <= 1.0):
        score = float(
            input("Score must be greater than 0.0 and less than 1.0: "))
    if score >= 0.9:
        print("Grade A")
    elif score >= 0.8:
        print("Grade B")
    elif score >= 0.7:
        print("Grade C")
    elif score >= 0.6:
        print("Grade D")
    else:
        print("Fail")
except ValueError as e:
    print(e)

'''
Output:  python3 chapter4_1_score.py
Enter your score: 9
Score must be greater than 0.0 and less than 1.0: 0.2
Fail

Enter your score: addskj
could not convert string to float: 'addskj'
'''
