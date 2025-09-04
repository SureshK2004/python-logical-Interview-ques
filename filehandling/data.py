with open ("data.txt","w") as f:
    f.write("Python Interview practice")

with open("data.txt","r") as f:
    c=f.read()
    print(c)

with open("data.txt","a") as f:
    f.write('\nSuresh is Preparing interview')

with open('data.txt', "r") as f:
    c=f.read().split()
    print(len(c))

word_count={}
with open("data.txt","r") as f:
    c=f.read().lower().split()

for i in c:
    if i in word_count:
        word_count[i]+=1
    else:
        word_count[i]=1
print(word_count)

c=max(word_count, key=word_count.get)
print(c)

c=0
with open("data.txt","r") as f:
    d=f.read()
    for i in d:
        if "interview" in d:
            c+=1
print("count the word in 'interview' ",c)