file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'a')

for line in file1.readlines():
    file2.write(line)

file1.close()
file2.close()


'''
file1.txt
Hello World
Hi, How are you?
This is file 1.

file2.txt
Hi there!
This is file2.
I am going to copy contents of file1.txt into this file.

Output: python3 chapter2_4_file.py

cat file2.txt
Hi there!
This is file2.
I am going to copy contents of file1.txt into this file.
Hello World
Hi, How are you?
This is file 1.
'''