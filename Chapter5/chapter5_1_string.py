class StringClass:
    def get_String(self):
        string_name = input("Enter a string name: ")
        self.string_name = string_name

    def print_String(self):
        print(self.string_name.upper())


if __name__ == '__main__':
    user1 = StringClass()
    print("Created a user: %s" % user1)
    user1.get_String()
    user1.print_String()


'''
Output: python3 chapter5_1_string.py

Created a user: <__main__.stringClass object at 0x7f2d742b0710>
Enter a string name: hi there!
HI THERE!
'''
