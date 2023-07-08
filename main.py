# Function take value from user and check if the value is positive
def takePositiveValue():
  n = -1
  while n < 0:
    n = int(input("Please enter a positive value: "))
  return n


###############
# Exercise 1: #
###############

def calculateFactorial():
  # Take value from user and check if the value is positive
  value = takePositiveValue()
  factorial = 1
  # Check if the value is 0 (the factorial of 0 is 1)
  if value == 0:
    return 1
# If the value is different than 0 do the factorial
  else:
    for i in range(value):
      factorial = factorial * (i + 1)  # i start from 0
  return factorial

# Excute the factorial of value
print(calculateFactorial())

###############
# Exercice 2: #
###############

def findDivisors():
  # Take number from user and check if the number is positive
  num = takePositiveValue()
  # Open a list
  l = []
  for i in range(num):
    # Find all divisors
    if ((num % (i + 1)) == 0):
      # Store divisors in the list
      l.append(i + 1)
  return l

# Excute the list of divisors
print(findDivisors())

###############
# Exercise 3: #
###############

def reverseString():
  str1 = input("Enter a string: ")
  return str1[len(str1)::-1]


print(reverseString())

###############
# Exercise 4: #
###############

def findEvenNumber():
  # Open two lists
  list1 = []
  list2 = []
  # Take the number of items from user
  print("How many items do you want ")
  # Check if the number entered is positive
  number_of_items = takePositiveValue()
  for i in range(number_of_items):
    # Take numbers from user
    num = int(input("what is the number you want to add "))
    # Add the numbers to a list
    list1.append(num)
  for i in range(len(list1)):
    # Find the even numbers from the original list
    if (list1[i] % 2 == 0):
      # Store the even numbers in a new list
      list2.append(list1[i])
  return list2


# Excute the new list
print(findEvenNumber())

###############
# Exwecise 5: #
###############

def checkPassword(password):
  # Check password length
  if (len(password) >= 8):
    uppercase = False
    lowercase = False
    number = False
    special = False

    for i in password:
      # Check for one uppercase letter
      if (i.isupper()):
        uppercase = True
    # Check for one lowercase letter
      if (i.islower()):
        lowercase = True
    # Check for one number
      if i.isdigit():
        number = True
    # Check for one special character
      if (not i.isalnum()):
        special = True

    return lowercase and uppercase and number and special

  else:
    return False


password = input("Enter a password: ")
if checkPassword(password):
  print("Strong password")
else:
  print("Weak password")
