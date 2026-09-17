#Main Program
name = input("Enter your name: ")
height_cm = float(input("Enter your height in centimeters: "))
height_m = height_cm / 100
height_inch = height_cm / 2.54
print(f"Hello, {name}!")
print(f"Your height in meters is: {height_m:.2f} m")
print(f"Your height in inches is: {height_inch:.2f} in")
print(f"Taller than 180cm: {height_cm>180}")
#Ext
print(f"That is {height_inch//12:.0f} feet and {height_inch%12:.2f} inches tall.")