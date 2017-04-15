string = input("Enter a string: ")
low_count, up_count = 0, 0

for i in string:
    if i.islower():
        low_count += 1
    elif i.isupper():
        up_count += 1
    else:
        pass

print("No. of Uppercase letters: %d" % up_count)
print("No. of Lowercase letters: %d" % low_count)


'''
Output:  python3 chapter2_5_casecount.py

No. of Uppercase letters: 3
No. of Lowercase letters: 12
'''
