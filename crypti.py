def getCipher():
    print('Enter the message to decrypt:')
    cipherText = raw_input()

    print('Enter your key shift:')
    cipherKey = int(raw_input())
    keySize = 26
    transText = ''

    for ch in cipherText:
        if ch.isalpha():
            shift = ord(ch)
            shift += cipherKey
            if ch.isupper():
                if shift > ord('Z'):
                    shift -= keySize
                elif shift < ord('A'):
                    shift += keySize
            elif ch.islower():
                if shift > ord('z'):
                    shift -= keySize
                elif shift < ord('a'):
                    shift += keySize
            transText += chr(shift)
        else:
            transText += ch
    return transText

print(getCipher())
