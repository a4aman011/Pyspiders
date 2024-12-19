# l=[10,2,50,20,6,25]
# for i in range(len(l)):
#     for j in range(len(l)):   
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)


l=[10,2,50,20,6,25]
c=0
for i in range(len(l)):
    for j in range(len(l)-1): 
        print(l,c)  
        if l[j]>l[j+1]:
            l[j+1],l[j]=l[j],l[j+1]
        c+=1
print(l)








# 7795004994