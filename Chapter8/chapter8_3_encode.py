import base64
plaintext = input("Enter a string to encode: ")

encoded = base64.b64encode(bytes(plaintext.encode('utf-8', "strict")))
decoded = base64.b64decode(encoded)
print("Encoded string: %s and Decoded string: %s" % (encoded, decoded))

'''
Output: python3 chapter8_3_encode.py
Enter a string to encode: hey there
Encoded string: b'aGV5IHRoZXJl' and Decoded string: b'hey there'
'''
