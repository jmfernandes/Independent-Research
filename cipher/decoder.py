letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

input = raw_input("input the name of the file: ")
filepath = 'Encrypted Documents/' + str(input)
stuff = open(filepath,'r')
data = list(stuff.read())
for i in range(len(data)):
    distance = 1
    if data[i] in letters:
        position = letters.index(data[i])
        difference = position - distance
        if difference < 0:
            data[i] = letters[len(letters) + difference]
        else:
            data[i] = letters[difference]
    elif data[i] in capital:
        position = capital.index(data[i])
        difference = position - distance
        if difference < 0:
            data[i] = capital[len(letters) + difference]
        else:
            data[i] = capital[difference]
    else:
        pass
stuff.close
print ''.join(data)