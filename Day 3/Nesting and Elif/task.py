print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input('what is your age?'))
    if age <= 18:
        print("please pay$7.")
    elif age<=12:
        print("please pay$5")

    else:
        print("please pay$15")
else:
    print("Sorry you have to grow taller before you can ride.")

print("BMI Interpretations")
value=int(input("enter your weight."))
if value < 18.5:
    print("underwight: not included")
elif value >= 18.5 and value <25:
    print("normal weight: included")
else:
    print("overweight")