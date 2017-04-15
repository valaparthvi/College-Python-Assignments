number = int(input("Enter a number to check if it is prime or not.\n"))
if number == 0 or number == 1:
    print('''
    %d is neither prime or composite.
    Primes must have only 2 factors, 1 and itself.
    Composite numbers have more than 2 factors.
    %d obeys neither of these rules because they have only 1 factors'''
          % (number, number))
else:
    for i in range(2, number):
        if number % i == 0:
            print("number is not prime")
            break
    else:
        print("The number is prime.")


'''
Output: python3 chapter1_3_prime.py

Enter a number to check if it is prime or not.
13
The number is prime.

Output: python3 chapter1_3_prime.py

Enter a number to check if it is prime or not.
1

    1 is neither prime or composite.
    Primes must have only 2 factors, 1 and itself.
    Composite numbers have more than 2 factors.
    1 obeys neither of these rules because they have only 1 factors

Enter a number to check if it is prime or not.
16
number is not prime
'''
