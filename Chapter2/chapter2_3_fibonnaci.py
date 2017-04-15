number = int(input("Enter a number: "))


def recur_fib(n):
    if n <= 1:
        return n
    else:
        return(recur_fib(n - 1) + recur_fib(n - 2))


for i in range(number):
    print(recur_fib(i))


'''
Output: python3 chapter2_3_fibonnaci.py

Enter a number: 9
0
1
1
2
3
5
8
13
21
'''
