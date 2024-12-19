# n=int(input("n: "))
# l=[0,1]
# for i in range(n-2):
#         a=l[-2]+l[-1]
#         l.append(a)
# print(l)

# n=int(input("n: "))
# l=[0,1]
# for i in range(n-2):
#         l.append(l[i]+l[i+1])
# print(l)


# n=int(input("n: "))
# l=[]
# a=0
# b=1
# for i in range(n):
#         l+=[a] #l.append(a)
#         c=a+b
#         a=b
#         b=c
# print(l)
# a="badac"
# res=""
# for i in range(len(a)):
#     for j in range(i+1,len(a)+1):
#         if a[i:j]==a[i:j][::-1]:
#             if len(a[i:j])>len(res):
#                 res=a[i:j]
# print(res)

# a="abcd"
# res=[""]
# for i in a:
#     values=[]
#     for j in res:
#         values+=[j+i]
#     res.extend(values)
# res.sort(key=len)
# print(res[1:])
# print(max(res,key=len))



a=['flow','flower','flight']
res=" "
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j]==a[j][i] or a[i][i]==a[j][j]:
            res+=a[i][j]
            
print(res)