def cipher():
    ans_start = input("Do you want to start?\n")
    ans_start = ans_start.upper()
    while(ans_start in 'YES'):
        print("What do you prefer to do?")
        ans = input("Press E to Encrypt. Press D to Decrypt: ")
        ans = ans.upper()

        if(ans == 'E'):
            user_input = input("Enter the text you want to Encrypt: ")
            intab = 'abcdefghijklmnopqrstuvwxyz'
            outtab = 'zyxwvutsrqponmlkjihgfedcba'
            encryption = ''
            encryption = encryption.maketrans(intab, outtab)
            print("Encrypted code is:")
            print(user_input.translate(encryption))

        elif(ans == 'D'):
            user_input = input("Enter the text you want to Decrypt: ")
            intab = 'zyxwvutsrqponmlkjihgfedcba'
            outtab = 'abcdefghijklmnopqrstuvwxyz'
            decryption = ''
            decryption = decryption.maketrans(intab, outtab)
            print("Decrypted code is:")
            print(user_input.translate(decryption))

        else:
            print("Please enter 'E' to Encrypt or 'D' to Decrypt.")
        ans_start = input("Do you want to do it again?")
        ans_start = ans_start.upper()


if __name__ == '__main__':
    cipher()

'''
Output: python3 chapter8_2_monoalphabeticCipher.py
Do you want to start?
yes
What do you prefer to do?
Press E to Encrypt. Press D to Decrypt: e
Enter the text you want to Encrypt: hey there
Encrypted code is:
svb gsviv
Do you want to do it again?y
What do you prefer to do?
Press E to Encrypt. Press D to Decrypt: d
Enter the text you want to Decrypt: svb gsviv
Decrypted code is:
hey there
Do you want to do it again?n
'''
