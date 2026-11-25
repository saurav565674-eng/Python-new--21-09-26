# arr=[100,101,100,102,101,100]
# freq=[0]*4 
# for i in arr:
#     freq[i-100]+=1
# for i in range(len(freq)):
#     print(f"{i+100}occurs {freq[i]}times")
# print(freq)

arr=[-4,-2,1,0,-2,1,3,-4]
freq=[0]*8
for i in arr:
    freq[i+4]+=1
for i in range(len(freq)):
    print(f"{i-4}occurs {freq[i]}times")
