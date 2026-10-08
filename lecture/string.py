text = " function of python"

#strip function remove space from the sentence starting and end
print("strip :", text.strip())

# all letter are capitalize
print("upper :" ,text.upper())

#all lower letter are lower case
print("lower :",text.lower())

#split the sentence into separate word my dispalr in list form
print("split :",text.split())

#capitilize start letter of each word
print(" capitalization :",text.capitalize())

#count the specific letter 
print ("count :" ,text.count("n"))
#
print("partition :",text.partition("of"))
print("replace :",text.replace("of","to"))
print("startswitch :",text.startswith("f"))
print("endswitch :",text.endswith("n"))
print("find :",text.find("of"))

#create list of 10 no 
li=[20,30,57,34,64,84,56,22,98,53]
letter=['sam','dex','get','ruffalo']

#print the sum of last 4 element on the list
print ("last no of the list sum :",sum(li[-4:]))

#find out he difference betwwn max and min element of the list
diff = sorted(li)[-1]-sorted(li)[0]
print("diff between max and min :",diff)

#insert the no in a list at 6 th positin this no must be 1/3 of no stored at 4th poisition 
li.insert(5,li[3]/3)
print(" insert :",li)

print(sorted(letter))

#calculate avg score and flag pass/fil
# students={
#   101:{"name":"hatch","scores":[70,53,68]}
# } 
# for sid,details in students.itmes():
#   avg = sum (details['scores'])/len(details['scores'])
#   details['average']=avg
#   details['passed']=avg>=50

  #guess random no

import random
guess = True
while not guess:
  user =guess(0,2000)
  num = int (input("enrt no :"))
 
  if user == num:
     print("you guessed right")
  else:
    print("try again")



name="saurav"
vowels =["a",'e',"i","o","u"]
for v in vowels:
  name=name.replace([vowels],"z")
  print(name)

#create a list of no and string 
li :list[str]=[]
for i in range(5):
  str=input("enter element")
  if str.isdigit():
    li.append(int(str))
  else:
    li.append(str)

aplhalist=[]
numlist=[]
for item in li:
  if item.isdigit():
    numlist.append(item)
  else:
    aplhalist.append


#aceept the values from user
#separate the list from the max no
#display the name in desc sorted order