#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))

percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

percent_decimal = percent/100 + 1

#Each person should pay (150.00 / 5) * 1.12 = 33.6
people = int(input("How many people to split the bill? "))

#Format the result to 2 decimal places = 33.60
bill_per_person = round( ((bill/people)*percent_decimal), 2 )


print(f"Each person should pay: ${bill_per_person}")

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal

#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
