def selection_sort(items):
    for step in range(len(items)):
        location_of_smallest = step
        for location in range(step, len(items)):
            if items[location] < items[location_of_smallest]:
                location_of_smallest = location
        items[step], items[location_of_smallest] = items[
            location_of_smallest], items[step]
    print("Sorted list is: %s" % items)


if __name__ == '__main__':
    num = int(input("Enter number of elements: "))
    lst = [int(input("Number at %d position: " % i)) for i in range(num)]
    selection_sort(lst)
