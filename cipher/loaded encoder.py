#this takes a txt file and encodes it. Take an ODT file and save as txt file. Save the document in plain documents and when asked for the file name, enter the name including .txt. The script will then same the txt into finished documents folder.

stuff = open('loaded.txt','r')
data = list(stuff.read())

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capital = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

input2 = raw_input("input the name of the text file: ")
filepath = 'Plain Documents/' + str(input2)
stuff = open(filepath,'r')
data = list(stuff.read())

input = raw_input("input codeword to encrypt file: ")
code = list(input)


counting = 0
reset = 0

for i in range(len(data)):
    if counting%(len(code)) ==0 and i!=0:
        counting = 0
    else:
        pass
    if code[counting] in letters or code[counting] in capital:
        pass
    else:
        print "\n ERROR: not a valid codeword. No letters or special characters allowed. \n"
        exit()
    if data[i] in letters or data[i] in capital:
        if code[counting] in letters:
            index = letters.index(code[counting])
        else:
            index = capital.index(code[counting])
    else:
        index = 30
    if index == 30:
        pass
    else:
        if data[i] in letters:
            position = letters.index(data[i])
            difference = position + index
            if difference >= len(letters):
                data[i] = letters[difference - len(letters)]
            else:
                data[i] = letters[difference]
        else:
            pass
        if data[i] in capital:
            position = capital.index(data[i])
            difference = position + index
            if difference >= len(capital):
                data[i] = capital[difference - len(letters)]
            else:
                data[i] = capital[difference]
        else:
            pass
        counting = counting + 1

print ''.join(data)

filepath2 = 'Finished Documents/' + str(input2)

myfile = open(filepath2,'w')

myfile.write(''.join(data))

myfile.close()

