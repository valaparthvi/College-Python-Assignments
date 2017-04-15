number_of_elements = int(input("Enter total number of elements: "))

print("Start entering numbers...")
lst = [input() for i in range(number_of_elements)]

print(list(set(lst)))

'''
Output: python3 chapter2_1_unique.py

Enter total number of elements: 5
Start entering numbers...
14
13
1
13
14
['1', '13', '14']
'''
