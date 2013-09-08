
def main():
    mymessage ='I like the color purple'
    mykey = 4
    ciphertext = decrypt(mykey,mymessage)

def decrypt(key,message):
    ciphertext = [''] * key
    for i in range(key):
        j = i
        while j < len(message):
            ciphertext[i] += message[j]
            j += key

    print ''.join(ciphertext)

if __name__ == '__main__':
    main()