import os


hello = open(os.path.join(os.getcwd(), 'file.txt'))

print(hello.readline())
