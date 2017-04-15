def add_to_list_in_dict(thedict, listname, element):
    try:
        lst = thedict[listname]
        print("%s already has %d elements." % (listname, len(lst)))
    except KeyError:
        thedict[listname] = []
        print("Created %s" % listname)
    else:
        thedict[listname].append(element)
        print("Added %s to %s" % (element, listname))
    finally:
        print("thedict = %s \nlistname = %s \nelement = %s" %
              (thedict, listname, element))


if __name__ == '__main__':
    thedict = {'l1': [1, 2, 3], 'l2': [4, 5, 6]}
    print("\n\tFunction called FIRST time:")
    add_to_list_in_dict(listname='l2', thedict=thedict, element=10)
    print("\n\tFunction called SECOND time:")
    add_to_list_in_dict(listname='l3', thedict=thedict, element=7)

'''
Output:  python3 chapter4_3_keyerror.py

    Function called FIRST time:
l2 already has 3 elements.
Added 10 to l2
thedict = {'l1': [1, 2, 3], 'l2': [4, 5, 6, 10]}
listname = l2
element = 10

    Function called SECOND time:
Created l3
thedict = {'l1': [1, 2, 3], 'l3': [], 'l2': [4, 5, 6, 10]}
listname = l3
element = 7
'''
