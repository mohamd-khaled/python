operator = input("Please choose an arithmetic operation (1:+ 2:- 3:* 4:/ 5:** 6:%)")
num1 = float(input("Please enter the first number"))
num2 = float(input("Please enter the second number"))


if operator == "+" or operator == "1":
    result = num1 + num2
    print (result)
    
elif operator == "-" or operator == "2":
    result = num1 - num2
    print (result)
    
elif operator == "*" or operator == "3":
    result = num1 * num2
    print (result)
    
elif operator == "/" or operator == "4":
    result = num1 / num2
    print (result)
    
elif operator == "**" or operator == "5":
    result = num1 ** num2
    print (result)
    
elif operator == "%" or operator == "6":
    result = num1 % num2
    print (result)
    
else:
    print ("You enteres wrong operation")
    