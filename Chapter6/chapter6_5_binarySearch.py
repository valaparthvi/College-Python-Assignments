def binarySearch(lst, search_element):
    mid = len(lst) // 2
    if search_element == lst[mid]:
        print(True)
    elif search_element in lst[:mid]:
        print(True)
    elif search_element in lst[mid + 1:]:
        print (True)
    else:
        print(False)


if __name__ == '__main__':
    number = int(input("Enter total no. of elements: "))
    print("Enter elements")
    lst = [int(input()) for i in range(number)]
    search_element = int(input("Enter search element: "))
    binarySearch(lst, search_element)


'''
Output: python3 chapter6_5_binarySearch.py
Enter total no. of elements: 6
Enter elements
12
13
14
12
11
15
Enter search element: 11
True

Enter total no. of elements: 5
Enter elements
1
2
3
4
5
Enter search element: 6
False

'''
