import shelve

shelFile = shelve.open('data')

print(shelFile['cats'])
shelFile.close()