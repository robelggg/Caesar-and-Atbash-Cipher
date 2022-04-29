alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']

reverse = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
           'e', 'd', 'c', 'b', 'a']


def CaesarEncipher():
    i = 0
    x = 0
    m = ""
    message = input("Enter message here (A - Z): ").lower().replace(" ", "")
    key = int(input("Enter the key: "))
    for i in range(key):
        if x < 1:
            alpha.append(alpha[x])
            alpha.pop(x)
        i += 1
    for letter in message:
        n = alpha.index(letter)
        m += alphabet[n]
    print(m)


def CaesarDecipher():
    i = 0
    x = 0
    m = ""
    message = input("Enter message here (A - Z): ").lower().replace(" ", "")
    key = int(input("Enter the key: "))
    for i in range(key):
        if x < 1:
            alpha.append(alpha[x])
            alpha.pop(x)
        i += 1
    for letter in message:
        n = alphabet.index(letter)
        m += alpha[n]
    print(m)


def atbashEncipher():
    m = ""
    message = input("Enter message here (A - Z): ").lower().replace(" ", "")
    for letter in message:
        n = reverse.index(letter)
        m += alphabet[n]
    print(m)


def atbashDecipher():
    m = ""
    message = input("Enter message here (A - Z): ").lower().replace(" ", "")
    for letter in message:
        n = alphabet.index(letter)
        m += reverse[n]
    print(m)


x = int(input("Choose One of the following: \n1. For Caesar Cipher Encryption\n2. For Caesar Cipher Decryption \n3. "
              "For Atbash Cipher Encryption \n4. For Atbash Cipher Decryption \n"))

if x == 1:
    CaesarEncipher()
elif x == 2:
    CaesarDecipher()
elif x == 3:
    atbashEncipher()
elif x == 4:
    atbashDecipher()
else:
    print("error try again")
