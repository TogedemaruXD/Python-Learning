list = ["apple","orange","mango"]
x = False
print("Welcome to the Supermarket, what would you like to buy? ")
print("Here is what you have in the shopping list right now. ")
print(list)
while x == False:
  userResponse=input("Do you want to add, remove or print the list? ")
  
  if userResponse == "add":
    add = input("what would you like to add? ")
    list.append(add)
    check = input("Is there anything else you would like to do? yes/no ")
    if check == "no":
      break

  elif userResponse == "remove":
    remove = input("What would you like to remove? ")
    list.remove(remove)
    check = input("Is there anything else you would like to do? yes/no ")
    if check == "no":
      break
  
  elif userResponse == "print":
    print(list)
    check = input("Is there anything else you would like to do? yes/no ")
    if check == "no":
      break
  
  elif userResponse =="stop":
    break
  
  else:
  print("You misspelled something! ")