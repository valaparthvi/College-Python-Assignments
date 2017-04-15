import re


def text_match(text):
    patterns = r'^ab+?'
    if re.search(patterns, text):
        print('Found a match!')
    else:
        print('Not matched!')


if __name__ == '__main__':
    text = input("Enter a text: ")
    text_match(text)

'''
Output:  python3 chapter7_2_ab.py
Enter a text: a
Not matched!

Enter a text: ab
Found a match!
'''
