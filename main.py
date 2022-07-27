# Area / Perimeter Python Tool - Created by Liam Pettigrew

def main():
  print(1)

# COMMIT 1 - Added copyright information and welcome message.
# Asks the user if they wish to either continue to the shape selection (main) or view the instructions.
# If the user wishes to view the instructions, the program shows a list of information about the program.
# Once the user finishes with the instructions, they are able to continue to main.

print("Ⓒ Area & Perimeter Calculator Tool Python Program created and authorised by Liam Pettigrew for personal and educational use.")
print("Ⓒ All efforts that went into this program and relating documents are rightfully belonged to Liam Pettigrew.")
print("Ⓒ Program first created in July 2022 for Fraser High School.")
print()
print("Welcome to Area & Perimeter Calculator Tool.")
print("Do you wish to view the instructions to the program or continue to the shape selection?")
print()
print(" - Instructions")
print(" - Continue")
instructionsOrContinue = input()
  
if instructionsOrContinue == "continue" or instructionsOrContinue == "Continue":
  main()

elif instructionsOrContinue == "instructions" or instructionsOrContinue == "Instructions":
  print()
  print("PROGRAM INSTRUCTIONS")
  print()
  print("The Area & Perimeter Calculator Tool, created by Liam Pettigrew, is an excellent way for students to check their mathematics work.")
  print("This program offers a list of rectangle, triangle, circle, and parrallelogram. You can then input the known dimenstions, and the program will fully work out the area and perimeter.")
  print()
  print("Are you ready to continue to the shape selection?")
  print()
  print(" - Continue")
  continueAfterInstructions = input()
  if continueAfterInstructions == ("Continue") or continueAfterInstructions == ("continue"):
    main()