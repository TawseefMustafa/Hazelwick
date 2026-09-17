#Main Program
while True:
    choice = int(input("Choose to work with a 3 or 4 digit number: "))
    match choice:
        case 3:
            num = int(input("Enter a 3 digit number: "))
            hundreds = num//100
            tens = (num%100)//10
            units = num - ((100*hundreds)+(10*tens))
            print(f"Hundreds: {hundreds}")
            print(f"Tens: {tens}")
            print(f"Units: {units}")
            print(f"Sum of digits: {hundreds+tens+units}")
            num_rev = (units*100)+(tens*10)+(hundreds)
            print(f"Reversed: {num_rev}") 
#470 Reversed is 074, but the first 0 in the hundreds place is not significant, therefore it means nothing and since i did not specify a number of digits
#Therefore Python only displays the significant part '74'
#If i specify that i want 3 digits displayed (num_rev:.03d), i will receive 074
            print(f"Even Number: {num % 2 == 0}")
#Ext
        case 4:
            num = int(input("Enter a 4 digit number: "))
            thousands = num//1000
            hundreds = (num%1000)//100
            tens = (num%100)//10
            units = num%10
            print(f"Thousands: {thousands}")
            print(f"Hundreds: {hundreds}")
            print(f"Tens: {tens}")
            print(f"Units: {units}")
            print(f"Sum of digits: {thousands+hundreds+tens+units}")
            num_rev = (units*1000)+(tens*100)+(hundreds*10)+thousands
            print(f"Reversed: {num_rev}") 
            print(f"Even Number: {num % 2 == 0}")
        case _:
            break
print("Error")