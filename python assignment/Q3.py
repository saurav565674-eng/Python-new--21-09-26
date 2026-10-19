#reading sentence
sentence = input("Enter a sentence: ")
# ceat empty array
words = []
longest_word= ""
#traversing array of senence by spliting them
for word in sentence.split():
    #appending word 
    words.append(word)
    #checking for largest no
    if len(word)>len(longest_word):
        longest_word = word

print(f"Longest word: {longest_word}")