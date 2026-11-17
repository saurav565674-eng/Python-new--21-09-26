#print sum of first 10 even no
# sum = 0
# for i in range (1,11,2):
#   sum += i
# print(sum)

#accept 2 values s and n .print square of first n nostarting from s
# s= int(input("enter no"))
# n= int(input("enter no"))
# for i in range(s,n+s):
#   print(i*i)

#accept sentence from user and count the vowels(easy)
# n = str(input("enter sentence"))
# vowels="aeiou"
# count=0
# for i ,ch in enumerate(n):
#   if ch in vowels or ch in vowels.upper():
#     count+=1
# print(count)

#accept sentence from user and count the vowels(medium)
# n = str(input("enter sentence"))
# vowels="aeiou"
# repeat={}
# count=0
# for i ,ch in enumerate(n):
#   if ch in vowels or ch in vowels.upper():
#     count+=1
#     if ch in 
# print(count)
# print(repeat)

#remove duplicate from list
# li=[5,5,4,6,84,7,7]
# unique=[]
# for i in li:
#   if i not in unique:
#     unique.append(i)
#   print(unique)

#reverse the lists
# li2=[5,3,6,3,5]
# li2.reverse()
# print(li2)

#print the pattern
# n=3
# for i in range(1,n+1):
#   print("*"*i)

#reverse the string
# s = input("enter string : z")
# for i in range(len(s) -1 ,-1,-1):
#   print(s[i],end="")
# print()

#center pattern
# n=int(input("enter :"))
# for i in range(1,n+1):
#   print("  "*((n+1)-i),end="")
#   print(" *  "*i)

#center pattern with alternate symbol
n=int(input("enter :"))
for i in range(1,n+1):
  print("  "*((n+1)-i),end="")
  print(" *  "*i) if i%2==0 else print(" $  "*i)
