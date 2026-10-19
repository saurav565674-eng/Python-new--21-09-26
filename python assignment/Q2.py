#open file
with open("file1.txt","r") as f:
  n=f.readlines()

  #count the total no of lines
print("total number of lines  ",len(n) )
#using index fuction 1 to print the 2nd line
print("2nd line",n[1])
#using index fuction 3 to print the 4nd line
print("4th line",n[3])