#Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

#the first number is initially assumed to be the largest number
largest_number = number1

#Check if the second number is larger than the current largest_number and update the largest_number if needed.
if number2 > largest_number:
    largest_number = number2

#Check if the third number is larger than the current largest_number and update the largest_number if needed.
if number3 > largest_number:
    largest_number = number3

#Print the result
print("The largest number is:", largest_number)
