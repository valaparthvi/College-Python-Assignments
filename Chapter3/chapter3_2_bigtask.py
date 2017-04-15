l1 = [i for i in range(1, 11)]
l2 = [i for i in range(10, 101, 10)]
l3 = ['python', 'django', 'flask', 'string', 'function', 'classes']
l4 = {'l1': l1, 'l2': l2, 'l3': l3}
main_list = []
main_list.extend(l1)
main_list.extend(l2)
main_list.extend(l3)
l5 = l1 * 2

main_list.append(l5)

print("Occurence of 1 in main_list is %d" % (
    main_list.count(1) + main_list[-1].count(1)))


'''
Output:  python3 chapter3_2_bigtask.py

Occurence of 1 in main_list is 3
'''
