# Area / Perimeter Python Tool - Created by Liam Pettigrew

def main():
  # COMMIT 2 - Added the main() shape selection, where the user can choose to select either a
  # rectangle, triangle, circle, or a parallelogram. I have also implemented answer-checkers throughout
  # the code, so that the program responds to invalid answers.
  print()
  print("SHAPE SELECTION")
  print("Please enter the shape you are wishing to solve.")
  print()
  print(" - Rectangle \n - Triangle \n - Circle \n - Parallelogram")
  whichShape = input()
  if whichShape == "Rectangle" or whichShape == "rectangle":
    print("Please enter the dimensions to this rectangle.")
    
  elif whichShape == "Triangle" or whichShape == "triangle":
    print("Please enter the dimensions to this triangle.")
    
  elif whichShape == "Circle" or whichShape == "circle":
    print("Please enter the dimensions to this circle.")
    
  elif whichShape == "Parallelogram" or whichShape == "parallelogram":
    print("Please enter the dimensions to this parallelogram.")
    
  else:
    print("This is not a valid shape. Please try again.")
    main()

# COMMIT 1 - Added copyright information and welcome message.
# Asks the user if they wish to either continue to the shape selection (main) or view the instructions.
# If the user wishes to view the instructions, the program shows a list of information about the program.
# Once the user finishes with the instructions, they are able to continue to main.

print("Ⓒ Area & Perimeter Calculator Tool Python Program created and authorised by Liam Pettigrew for personal and educational use.")
print("Ⓒ All efforts that went into this program and relating documents are rightfully belonged to Liam Pettigrew.")
print("Ⓒ Program first created in July 2022 for Fraser High School.")
print()
print("Welcome to Area & Perimeter Calculator Tool.")
def start():
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
    print("This program offers a list of rectangle, triangle, circle, and parallelogram. You can then input the known dimenstions, and the program will fully work out the area and perimeter.")
    print()
    print("Are you ready to continue to the shape selection?")
    print()
    def afterInstructionsLoop():
      print(" - Press Enter")
      continueAfterInstructions = input()
      if continueAfterInstructions == (""):
        main()
      else:
        print("This is not a valid answer.")
        afterInstructionsLoop()
    afterInstructionsLoop()
  
  else:
    print()
    print("This is not a valid response. Please try again.")
    print()
    start()
start()