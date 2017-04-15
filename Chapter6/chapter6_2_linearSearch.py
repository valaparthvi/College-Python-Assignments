def linearSearch(lst, element):
    try:
        if element not in lst:
            raise(ValueError)
    except ValueError:
        print("%d is not in the list %s" % (element, lst))
    else:
        for position, number in enumerate(lst):
            if number == element:
                if lst.count(element) > 1:
                    print("First Position of %d is %d" %
                          (element, lst.index(element)))
                    break
                else:
                    print("Position of %d is %d" % (element, position))


if __name__ == '__main__':
    number_of_elements = int(input("Enter number of Elements: "))
    print("Enter the elements:")
    lst = [int(input()) for i in range(number_of_elements)]
    element = int(input("Enter search element: "))
    linearSearch(lst, element)

'''
Output: python3 chapter6_2_linearSearch.py
Enter number of Elements: 5
Enter the elements:
23
45
56
45
67
Enter search element: 45
First Position of 45 is 1

Enter number of Elements: 3
Enter the elements:
12
13
12
Enter search element: 13
Position of 13 is 1

Enter number of Elements: 4
Enter the elements:
12
45
34
56
Enter search element: 11
11 is not in the list [12, 45, 34, 56]

'''