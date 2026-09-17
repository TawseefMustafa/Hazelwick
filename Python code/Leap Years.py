#Main Program
#Years:
leap = False
year = int(input("Enter the current year"))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap")
    leap = True
else:
    print(f"{year} is not leap")
#Months:
months = [
    ["January","February","March","April","May","June","July","August","September","October","November","December"],
    [31,28,31,30,31,30,31,31,30,31,30,31]
]
if leap:
    months[1][1] += 1
num = int(input("Enter a month number(1-12)"))
print(f"{months[0][num-1]} of {year} has {months[1][num-1]} days")
