#to read file
with (open("file1.txt","r") as f):
    #create empty array
    words =[]
    #adding sentence into word
    words =  f.read().split()
# print lenght of word
print(f"Total words: {len(words)}")
# print unique word
print("Unique words: ",end="")
# print unique word by counting array
for word in words:
    if words.count(word)==1:
        print(word,end=" ")