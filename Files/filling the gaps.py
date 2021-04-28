import os, re

matchedFiles = []

for filename in os.listdir(os.getcwd()):
    x = re.compile(r'^spam(\d{3})')
    mo = x.search(filename)
    if mo != None :
        print(mo.group(1))
        matchedFiles.append(mo.group(1))

matchedFiles.sort()
print(matchedFiles)
i = 0

for elt in matchedFiles:
    print(int(matchedFiles[i]))
    newNum = []
    numFiles = int(matchedFiles[i+1]) - int(matchedFiles[i]) - 1
    if ( numFiles ) > 0 :
        for j in range(int(matchedFiles[i])+1, int(matchedFiles[i+1]) - 1):
            x = str(j)
            for k in range(3 - len(x)):
                x = '0' + x
            f = open('spam' + x + ".txt", "w+")

    i+=1