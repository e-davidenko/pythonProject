import os, os.path
input = input("Введите файл или директорию: ")
isfile = os.path.isfile(input)
if isfile:
    print("file")
elif isfile != "true" :
    ispath = os.path.isdir(input)
    if ispath:
        print("dir")
    else:
        print("not exist")