import os.path
path1 = input("Введите директорию для считывания")
dirs = []
dirs = os.listdir(path1)
for i in dirs:
    print(i)