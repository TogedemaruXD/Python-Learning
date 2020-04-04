x=input("Would you like the result to be C or F? ")
y=input("What is the temperature in degrees? ")
if x == "c":
  cresult = (float(y) * 1.8) + 32
  print("the temperature is " + str(cresult) + " degrees")
if x == "f":
  fresult = (float(y) - 32) * 1.8
  print("the temperature is " + str(fresult) + " degrees")
