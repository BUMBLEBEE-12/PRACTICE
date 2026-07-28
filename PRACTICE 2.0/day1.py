print("hello ")
name =input('whats your name?')
length = len(name)
for i in range(len(name)):
        if name[i] == " ":
             length = length - 1
print(length)