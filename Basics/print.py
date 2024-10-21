# # # # # # # print(10,20,30,40,sep="--",end="$")
# # # # # # # print(10,20,30,40,end="*")
# # # # # # # print(10,20,30,40,"love",sep="--")
# # # # # # # print('man')


# # # # # s="Iron man and spiderman are good friends"
# # # # # # # s1=s.rfind("a")
# # # # # # # print(s1)
# # # # # # # s2=s.rfind("a",2,7)
# # # # # # # print(s2)
# # # # # # # s3=s.rfind("1")
# # # # # # # print(s3)

# # # # # # s1=s.rsplit(" ")
# # # # # # print(s1)
# # # # # # s2=s.rsplit("a")
# # # # # # print(s2)
# # # # # # s3=s.rsplit("a",maxsplit=2)
# # # # # # print(s3)
# # # # # # s4=s.rsplit("man",1)
# # # # # # print(s4)

# # # # # # s="Iron man\n and spiderman\n are\n good friends"
# # # # # # print(s)
# # # # # # s1=s.splitlines()
# # # # # # print(s1)
# # # # # # s2=s.splitlines(False)
# # # # # # print(s2)

# # # # # s1=s.rpartition("z")
# # # # # print(s1)
# # # # # s2=s.rpartition("man")
# # # # # print(s2)

# # # # s="good"
# # # # print(len(s))
# # # # s1=s.center(10,"*")
# # # # print(s1,len(s1))


# # # s=" good "
# # # s1=s.rjust(10)
# # # print(s1,len(s1))
# # # s2=s.rjust(10,"^")
# # # print(s2,len(s2))

# # s="beautifull"
# # print(s.endswith("l"))
# # print(s.endswith("b"))
# # print(s.endswith("u",-3))
# # print(s.endswith("1"))

# s="panda"
# s1=s.zfill(5)
# print(s1)
# s2="-123"
# s3=s2.zfill(7)
# print(s3)
# s4="+123"
# s5=s4.zfill(8)
# print(s5)
# s6=s.zfill(7)
# s7=s.zfill(10)
# print(s6)
# print(s7)
# s8="%123"
# s9=s8.zfill(10)
# print(s9)


s="cherry's and apple's are red in color"
s1=s.replace("e","--")
print(s1)
s2=s.replace(" ","--",2)
print(s2)