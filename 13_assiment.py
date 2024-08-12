#warite a program to make a  algorithm calulator.

first_number = float(input("enter first number >"))
second_number = float(input("enter second number >"))
c =  input("enter your opreation")
if '+'in c:
    print(first_number+second_number)

elif'-'in c:
    print(first_number-second_number)

elif'*'in c:
  print(first_number*second_number)
  
elif'/'in c:
  if second_number != 0:
    print(first_number/second_number)
  else:
    print("zero is not divisible")
else:
   print("Invalid input")







#write a program to find input number is prime or composite.

# def is_prime(number):
#     if number <= 1:
#         return False
#     if number == 2:
#         return True
#     if number % 2 == 0:
#         return False
#     for i in range(3, int(number**0.5) + 1, 2):
#         if number % i == 0:
#             return False
#     return True

# # Get input from the user
# num = int(input("Enter a number: "))

# # Determine if the number is prime or composite
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is a composite number.")

