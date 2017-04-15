import re


def stringCheck(string):
    compiler = re.compile(r'[^a-zA-Z0-9.]')
    string = compiler.search(string)
    print("String contains only certain characters is: %s"
          % (not bool(string)))


if __name__ == '__main__':
    string = input("Enter a string: ")
    stringCheck(string)


'''
Output: python3 chapter7_1_re.py
Enter a string: uieuqwoie[]
String contains only certain characters is: False

Enter a string: fhasjkfhdsjkfh121312
String contains only certain characters is: True
'''
