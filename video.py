#Updated 1 Feb 2025
#Watch the video here: https://www.youtube.com/watch?v=YKxvDL3JxEA or follow the instructor led demo
#Implement all the code shown in the video.
#Modify the code so the checks from 12 and under for the $8 price tag
#and 62 and older for the $12 price tag.

print("welcome to the Menu Orderning Station")

costumerAge = int(input("What is the age of the costumer?"))

price = 0

if costumerAge < 10:
    price = 8
elif costumerAge >= 55:
    price = 9
else:
    price = 12

print(f"the cost for this costumer is ${price}.")

drinkYesNo = input("Add a drink? Y/N? ")

if drinkYesNo == "y":
    smallLarge = input("Small or Large? S/L ")
    if smallLarge == "L":
        price += 2
    else:
        price += 1
print(f"Total i: ${price}")