#open file
with open ("file1.txt","r") as f:
  
  s =f.read()
count=0

# the lines is store in 
for ch in s.lower():
  if ch in ["a","e","i","o","u"]:
    count+=1

print(f"vowels present in file {count}" )