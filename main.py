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
  # COMMIT 3 - Added the dimension selections to every individual shape, which correlates to the
  # properties of the particular shape. Program breaks after dimensions are input.
  if whichShape == "Rectangle" or whichShape == "rectangle":
    print("RECTANGLE DIMENSION SELECTION")
    print()
    rectangleHeight = input("Please enter the height: ")
    rectangleWidth = input("Please enter the width: ")
    
  elif whichShape == "Triangle" or whichShape == "triangle":
    def triangle():
      print("TRIANGLE DIMENSION SELECTION")
      print()
      print("What do you wish to find out?")
      print(" - Area")
      print(" - Perimeter")
      print(" - Both")
      triangleSelection = input()
      # COMMIT 4 - Added a more advanced triangle dimension selection to make it easier for the user.
      # The user can now select if they are wanting to find out the area, perimeter, or both before entering the calculations.
      if triangleSelection == "Area" or triangleSelection == "area":
        triangleBase = input("Please enter the width of the base: ")
        triangleHeight = input("Please enter the length of the height: ")
      elif triangleSelection == "perimeter" or triangleSelection == "Perimeter":
        triangleSide1 = input("Please enter the length of side 1: ")
        triangleSide2 = input("Please enter the length of side 2: ")
        triangleSide3 = input("Please enter the length of side 3: ")
      elif triangleSelection == "both" or triangleSelection == "Both":
        triangleSide1 = input("Please enter the length of side 1: ")
        triangleSide2 = input("Please enter the length of side 2: ")
        triangleSide3 = input("Please enter the length of side 3: ")
        triangleBase = input("Please enter the width of the base: ")
        triangleHeight = input("Please enter the length of the height: ")
      else:
        print("This is not a valid answer.")
        triangle()
    triangle()
      
    
  elif whichShape == "Circle" or whichShape == "circle":
    print("CIRCLE DIMENSION SELECTION")
    print()
    circleRadius = input("Please enter the radius: ")
    
  elif whichShape == "Parallelogram" or whichShape == "parallelogram":
    def parallelogram():
      print("PARALLELOGRAM DIMENSION SELECTION")
      print()
      print("What do you wish to find out?")
      print(" - Area")
      print(" - Perimeter")
      print(" - Both")
      parallelogramSelection = input()
      # COMMIT 4 - Added a more advanced parallelogram dimension selection to make it easier for the user.
      # The user can now select if they are wanting to find out the area, perimeter, or both before entering the calculations.
      if parallelogramSelection == "Area" or parallelogramSelection == "area":
        parallelogramBase = input("Please enter the width of the base: ")
        parallelogramHeight = input("Please enter the length of the height: ")
      elif parallelogramSelection == "perimeter" or parallelogramSelection == "Perimeter":
        parallelogramSide1 = input("Please enter the length of the side: ")
        parallelogramBase = input("Please enter the width of the base: ")
      elif parallelogramSelection == "Both" or parallelogramSelection == "both":
        parallelogramSide1 = input("Please enter the length of the side: ")
        parallelogramBase = input("Please enter the width of the base: ")
        parallelogramHeight = input("Please enter the length of the height: ")
      else:
        print("This is not a valid answer.")
        parallelogram()
    parallelogram()
    
    
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