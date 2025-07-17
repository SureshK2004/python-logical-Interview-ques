#write a python to read a file with multipl lines & split data by lines also split into word

#steps:1--read a file,2--split data by line, 3-- split into words

f=open("C:\\file.txt")
data=f.read()
print(data)

lines=data.split("\n")
print(lines)

split_words = []
for line in lines:
    split_words.extend(line.split(" "))
print(split_words)
