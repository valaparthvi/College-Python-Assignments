number_of_elements = int(input("Enter total number of items: "))
print("Every key must be unique. Enter keys: ")
keys = [input() for key in range(number_of_elements)]
print("Enter values: ")
values = [input() for value in range(number_of_elements)]

hash = {k: v for k, v in zip(keys, values)}
print(hash)

'''
Outpu: python3 chapter6_3_hashobj.py
Enter total number of items: 4
Every key must be unique. Enter keys:
a
b
c
d
Enter values:
1
2
3
4
{'b': '2', 'd': '4', 'a': '1', 'c': '3'}
'''
