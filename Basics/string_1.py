# # s="csk mi rcb srh"
# # v=''
# # l=[]
# # for i in s:
# #     if i!=" ":
# #         v+=i
# #     else:
# #         l.append(v)
# #         v=""
# # if v!="":
# #     l.append(v)
# # print(l)           #['csk', 'mi', 'rcb', 'srh']


# # s="csk mi rcb srh"
# # s=s.replace(" ",",")
# # print([s])

# # ANAGRAM
# a='silent'
# b='listen'
# for i in a:
#     if a.count(i)==b.count(b):


# s="programming"
# t=""
# for i in s:
#     if s.count(i)>=1:
#         if i not in t:
#             t+=i
# print(t)                     #progamin

s="teamA teamB teamC"
# c=''
# l=[]
# for i in s:
#     if i!=" ":
#         c+=i
#     else:
#         if c!=" ":
#             l.append(c)
#         c=' '
# if c!=" ":
#     l.append(c)
# print(l)
s1=''
l=[]
for i in s:
    if i!=" ":
        s1+=i
    else:
        if s1!=" ":
            l.append(s1)
        
if s1!=" ":
    l.append(s1)
print(l)
