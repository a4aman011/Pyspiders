# n = int(input("n: "))
# for i in range(0,n):
#     print(i**2)

year = int(input("year: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")
