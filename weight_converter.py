weight = float(input("Please enter the weight: "))
unit = input("what is the unit kilogram or bound? (K or L): ")

if unit == "L" or unit == "l":
    weight /= 2.205
    unit = "kg" 
    print(f"the weight = {round(weight,1)} {unit}")
    
elif unit == "K" or unit == "k":
    weight *= 2.205
    unit = "Lbs"
    print(f"the weight = {round(weight,1)} {unit}")

else:
    print("you entered something wrong")
    
    
 