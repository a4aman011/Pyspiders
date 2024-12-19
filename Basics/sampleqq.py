# PROGRAM 1

n = int(input())
if n%2!=0:
    print("Wierd")
elif n%2!=0 and 1<n<6:
    print("Not Wierd")
elif n%2==0 and 6<n<21:
    print("Wierd")
elif n%2==0 and n>20:
    print("Not Wierd")
else:
    print("not even nor odd")

# PROGRAM 2 - to check whether entered no. is divisible by 7 
# and multiple of 5 in given range

val = int(input("val: "))

if 1500<=val<=2700:
    if val%7==0 and val%5==0:
         print(f"{val} is divisible by 7 and multiple of 5 in range 1500 and 2700")
    else:
        print("not divisible and not in range")
else:
    print("Not in range")


# PROGRAM 3 - to enter all no. divisible by 7 and multiple of 5 
# between two given number

val = []
for i in range(1500, 2700):
    if i%7==0 and i%5==0:
        val.append(str(i))
        print(i,end=",")


