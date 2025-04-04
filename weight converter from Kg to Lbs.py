weight = float(input("Enter your weight"))
unit = input("kilograms or Pounds? (k or P): ")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."    
else:
    print(f"{unit} was not valid")
    
    print(f"Your weight is: {round(weight, 3)} {unit}")