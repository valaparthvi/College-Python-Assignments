class Person:
    TITLES = ['Mr', 'Ms', 'Mrs', 'Dr']

    def __init__(self, fname, lname, title, email):
        self.fname = fname
        self.lname = lname
        self.title = title
        self.email = email

    def titleValidate(self):
        try:
            if self.title not in self.TITLES:
                raise ValueError
        except ValueError:
            print("%s is an invalid title!" % self.title)


if __name__ == '__main__':
    person1 = Person("Joey", "Tribbiani", "Mr",
                     "joeydoesntsharefood@gmail.com")
    person1.titleValidate()
    person2 = Person("Chandler", "Bing", "Jr", "chandlerisa girl@friends.com")
    person2.titleValidate()

'''
Output: python3 chapter5_5_title.py
Jr is an invalid title!
'''
