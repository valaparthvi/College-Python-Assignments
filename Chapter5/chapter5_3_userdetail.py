user_lst = [('vibe', 'cisco@ramon.com', 15),
            ('john', 'john@watson.com', -1),
            ('sherlock', 'sherlock@holmes.com', 32),
            ('thearrow', 'oliver@queen.com', 40),
            ('theflash', 'barry@allen.com', 27),
            ('babychandler', 'chandler@bing,com', 15),
            ('emma', 'rachel@geller.com', 17),
            ('emma', 'emma@watson.com', 28)]

user_dict = dict()

for usr in user_lst:
    try:
        name, email, age = usr[0], usr[1], usr[2]
        if user_dict.get(name) != None:
            raise (KeyError)
        elif age < 0:
            raise(ArithmeticError)
        elif 0 <= age < 16:
            raise(ValueError)
        elif age >= 16:
            user_dict[name] = email
        else:
            pass
    except KeyError:
        print("Username %s already exists" % name)
    except ArithmeticError:
        print("%s, your age must be a positive integer." % name)
    except ValueError:
        print("%s, you are under 16." % name)
print(user_dict)


'''
Output:  python3 chapter5_3_userdetail.py
vibe, you are under 16.
john, your age must be a positive integer.
babychandler, you are under 16.
Username emma already exists
{'theflash': 'barry@allen.com', 'thearrow': 'oliver@queen.com', 'emma': 'rachel@geller.com', 'sherlock': 'sherlock@holmes.com'}
'''
