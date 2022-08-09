# Area / Perimeter Python Tool - Created by Liam Pettigrew
import math

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
    def rectangle():
      print("RECTANGLE DIMENSION SELECTION")
      print()
      # COMMIT 5 - Added the mathematics functions for the rectangle selection. Now, both the area and perimeter
      # is calculated for the rectangle based on the user's input. Question also returns if the user mistakenly inputs a letter.
      rectangleHeight = input("Please enter the height: ")
      rectangleWidth = input("Please enter the width: ")
      RHdigit = rectangleHeight.isdigit()
      RWdigit = rectangleWidth.isdigit()
      if RHdigit == False or RWdigit == False:
        print()
        print("Your answers need to be in numbers. Please try again.")
        print()
        rectangle()
      else:
        rectangleArea = float(rectangleHeight) * float(rectangleWidth)
        rectanglePerimeter = (float(rectangleHeight) + (float(rectangleWidth))) * 2
        print("The area of this rectangle is: " + str(rectangleArea))
        print("The perimeter of this rectangle is: " + str(rectanglePerimeter))
    rectangle()
    
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
      # Also returns the question if the user inputted an unknown response.
      if triangleSelection == "Area" or triangleSelection == "area":
        triangleBase = input("Please enter the width of the base: ")
        triangleHeight = input("Please enter the length of the height: ")
        # COMMIT 6 - Added mathematical functions to the triangle selection, for the area, perimeter, and both function.
        # Function returns if the user inputs a letter instead of a number.
        THdigit = triangleHeight.isdigit()
        TBdigit = triangleBase.isdigit()
        if THdigit == False or TBdigit == False:
          print()
          print("Your answers need to be in numbers. Please try again.")
          print()
          triangle()
        else:
          triangleArea = (float(triangleBase) * float(triangleHeight)) / 2
          print("The area of the triangle is: " + str(triangleArea))
      elif triangleSelection == "perimeter" or triangleSelection == "Perimeter":
        triangleSide1 = input("Please enter the length of side 1: ")
        triangleSide2 = input("Please enter the length of side 2: ")
        triangleSide3 = input("Please enter the length of side 3: ")
        TS1digit = triangleSide1.isdigit()
        TS2digit = triangleSide2.isdigit()
        TS3digit = triangleSide3.isdigit()
        if TS1digit == False or TS2digit == False or TS3digit == False:
          print()
          print("Your answers need to be in numbers. Please try again.")
          print()
          triangle()
        else:
          trianglePerimeter = float(triangleSide1) + float(triangleSide2) + float(triangleSide3)
          print("The perimeter of the triangle is: " + str(trianglePerimeter))
      elif triangleSelection == "both" or triangleSelection == "Both":
        triangleSide1 = input("Please enter the length of side 1: ")
        triangleSide2 = input("Please enter the length of side 2: ")
        triangleSide3 = input("Please enter the length of side 3: ")
        triangleBase = input("Please enter the width of the base: ")
        triangleHeight = input("Please enter the length of the height: ")
        TS1digit = triangleSide1.isdigit()
        TS2digit = triangleSide2.isdigit()
        TS3digit = triangleSide3.isdigit()
        THdigit = triangleHeight.isdigit()
        TBdigit = triangleBase.isdigit()
        if TS1digit == False or TS2digit == False or TS3digit == False or THdigit == False or TBdigit == False:
          print()
          print("Your answers need to be in numbers. Please try again.")
          print()
          triangle()
        else:
          triangleArea = (float(triangleBase) * float(triangleHeight)) / 2
          trianglePerimeter = float(triangleSide1) + float(triangleSide2) + float(triangleSide3)
          print("The area of the triangle is: " + str(triangleArea))
          print("The perimeter of the triangle is: " + str(trianglePerimeter))
      else:
        print("This is not a valid answer.")
        triangle()
    triangle()
      
    
  elif whichShape == "Circle" or whichShape == "circle":
    def circle():
      print("CIRCLE DIMENSION SELECTION")
      print()
      # COMMIT 7 - The circle mathematical functions have been inputted, which calculates both the area and
      # circumference of the circle, using the "math.pi" imported tool. Question returns if user mistakenly
      # inputs a letter instead of a number.
      circleRadius = input("Please enter the radius: ")
      CRdigit = circleRadius.isdigit()
      if CRdigit == False:
        print()
        print("Your answers need to be in numbers. Please try again.")
        print()
        circle()
      else:
        circleArea = math.pi * (float(circleRadius) * float(circleRadius))
        circlePerimeter = 2 * math.pi * float(circleRadius)
        print("The area of the circle is: " + str(circleArea))
        print("The circumference of the circle is: " + str(circlePerimeter))
    circle()
    
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
      # Also returns the question if the user inputted an unknown response.
      if parallelogramSelection == "Area" or parallelogramSelection == "area":
        parallelogramBase = input("Please enter the width of the base: ")
        parallelogramHeight = input("Please enter the length of the height: ")
        # COMMIT 8 - Added the mathematical functions for the parallelogram (for the area, perimeter, and both). Question
        # returns if the user inputs an invalid response. This concludes Phase Three, now that all mathematical functions
        # have been put in. However, after calculating each question, the program breaks.
        PBdigit = parallelogramBase.isdigit()
        PHdigit = parallelogramHeight.isdigit()
        if PBdigit == False or PHdigit == False:
          print()
          print("Your answers need to be in numbers. Please try again.")
          print()
          parallelogram()
        else:
          parallelogramArea = float(parallelogramBase) * float(parallelogramHeight)
          print("The area of the parallelogram is: " + str(parallelogramArea))
      elif parallelogramSelection == "perimeter" or parallelogramSelection == "Perimeter":
        parallelogramSide = input("Please enter the length of the side: ")
        parallelogramBase = input("Please enter the width of the base: ")
        PSdigit = parallelogramSide.isdigit()
        PBdigit = parallelogramBase.isdigit()
        if PSdigit == False or PBdigit == False:
          print()
          print("Your answers need to be in numbers. Please try again.")
          print()
          parallelogram()
        else:
          parallelogramPerimeter = 2 * (float(parallelogramSide) + float(parallelogramBase))
          print("The perimeter of the parallelogram is: " + str(parallelogramPerimeter))
      elif parallelogramSelection == "Both" or parallelogramSelection == "both":
        parallelogramSide = input("Please enter the length of the side: ")
        parallelogramBase = input("Please enter the width of the base: ")
        parallelogramHeight = input("Please enter the length of the height: ")
        PSdigit = parallelogramSide.isdigit()
        PBdigit = parallelogramBase.isdigit()
        PHdigit = parallelogramHeight.isdigit()
        if PBdigit == False or PHdigit == False or PSdigit == False:
          print()
          print("Your answers need to be in numbers. Please try again.")
          print()
          parallelogram()
        else:
          parallelogramArea = float(parallelogramBase) * float(parallelogramHeight)
          parallelogramPerimeter = 2 * (float(parallelogramSide) + float(parallelogramBase))
          print("The area of the parallelogram is: " + str(parallelogramArea))
          print("The perimeter of the parallelogram is: " + str(parallelogramPerimeter))
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