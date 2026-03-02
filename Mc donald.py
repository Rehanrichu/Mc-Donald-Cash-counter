print("   'WELCOME TO MCDONALDS'  ")# welcoming title
print(" ------------------------- ")
print("What do you want to eat") # asking what he want to eat
print("")
x = int(input(" burgers :  "))# customer burger count
y = int(input("fries : ")) # customer fries count
z = int(input("cola : ")) #customer cola count
# value of the food
burger = 100
fries = 50
cola = 10
total = (burger*x)+(fries*y)+(cola*z)
print("So you need ",x,"burgers,",y,"fries and ",z,"cola")
print("")
print("Calculating your total bill...")
print("The total will be $",total)
print("")
# a free dessert for over $600
if total > 600 :
    print("congratulation,you won a dessert")
else :
    print("you didn't win a dessert")
print("")
print("   Have a Nice Day  ")
