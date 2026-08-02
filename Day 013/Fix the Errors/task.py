try:
    age = int(input("How old are you?"))
except ValueError:
    print("Y have typed wrong no, plz try again with numerical ")
    age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")
