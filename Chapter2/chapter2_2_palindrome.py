word = input("Enter a word to check if it's palindrome: ").upper()

length = len(word)
count = 0
for i in range(length // 2):
    if word[i] != word[-(i + 1)]:
        count += 1
    else:
        pass

if count == 0:
    print("%s is Palindrome." % word)
else:
    print("%s is not Palindrome." % word)


'''
Output: python3 chapter2_2_palindrome.py

Enter a word to check if it's palindrome: goodoog
GOODOOG is Palindrome.
'''
