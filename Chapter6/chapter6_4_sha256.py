import hashlib

plaintext = b'Hello Monty Python'
hashobj = hashlib.sha256(plaintext)
ciphertext = hashobj.hexdigest()
print("Hashed value for %s is\n%s" % (plaintext, ciphertext))

'''
Output: python3 chapter6_4_sha256.py
Hashed value for b'Hello Monty Python' is
7c83feb5b1eaa7df236ae5dd3faad1a6f9c6c52ccb5a261b5935c716c23ed8c2
'''
