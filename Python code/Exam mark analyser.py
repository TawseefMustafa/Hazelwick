#Main Program
total = 0
count = 0
high_mark = 0
low_mark = 100
while True:
    mark = int(input("Enter a mark or -1 to finish"))
    if mark == -1:
        break
    elif mark < 0 or mark > 100:
        print("Invalid mark")
    else:
        total += mark
        count += 1
        if mark > high_mark:
            high_mark = mark
        if mark < low_mark:
            low_mark = mark
if count != 0:
    mean = total/count
    print(f"Valid marks entered: {count}")
    print(f"Mean average: {mean}")
    print(f"Highest: {high_mark}")
    print(f"Lowest: {low_mark}")
else:
    print("No valid marks entered")                                                                                                                                                   