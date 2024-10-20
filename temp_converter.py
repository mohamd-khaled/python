temp = float(input("Please enter the temperature: "))
unit = input("what is the unit celsius or fehrenheit? (C or F): ")

if unit == "C" or unit == "c":
    temp = round(((9*temp)/5)+32 , 1)
    unit = "F" 
    print(f"the temprature = {temp}°{unit}")
    
elif unit == "F" or unit == "f":
    temp = round((((temp - 32)*5))/9 , 1)
    unit = "C"
    print(f"the temprature = {temp}°{unit}")

else:
    print("you entered something wrong")
    
    
 