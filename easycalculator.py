num1 = float(input("Enter First Number: "))
asmd = str(input("Enter +,-,x,/: "))
num2 = float(input("Enter Second Number: "))
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
divided = num1 / num2
if asmd == "+" :
     print(add)
elif asmd == "-" :
     print(subtract)
elif asmd == "x" :
     print(multiply)
elif asmd == "/" :
     print(divided)
else :
     print("Invalid string") 