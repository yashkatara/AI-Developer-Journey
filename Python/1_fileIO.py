f = open("file.txt")
data = f.read()

if("twinkle" in data):
    print("yes twinkle is present in the file")
print(data)
f.close()