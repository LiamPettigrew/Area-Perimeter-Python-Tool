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
        calculations.append("Rectangle hieght: " + str(rectangleHeight))
        calculations.append("Rectangle width: " + str(rectangleWidth))
        rectangleArea = float(rectangleHeight) * float(rectangleWidth)
        calculations.append("Rectangle Area: " + str(rectangleArea))
        rectanglePerimeter = (float(rectangleHeight) + (float(rectangleWidth))) * 2
        calculations.append("Rectangle Perimeter " + str(rectanglePerimeter))
        print("The area of this rectangle is: " + str(rectangleArea))
        print("The perimeter of this rectangle is: " + str(rectanglePerimeter))

        # COMMIT 9 - Added individual path selections for each shape for after the calculations are shown. Once the user is finished, they can now choose
        # to solve another shape for the selected shape they're currently on (looping back to the function of the shape), or
        # choose another shape (returning back to the start of main()). A choice for the history of all calculations made has
        # also been included, however it hasn't been coded yet. The question returns if the user inputs an invalid answer.
        def pathAfterShapeFunc():
          print()
          print("What do you wish to do now?")
          print()
          print(" - A: Solve another rectangle")
          print(" - B: Choose another shape")
          print(" - C: View the history of all your calculations")
          pathAfterShape = input()
          if pathAfterShape == "A" or pathAfterShape == "a":
            rectangle()
          elif pathAfterShape == "b" or pathAfterShape == "B":
            main()
          elif pathAfterShape == "c" or pathAfterShape == "C":
            inputHistory()
          else:
            print("This is an invalid response. Please type the letter for your choice.")
            pathAfterShapeFunc()
        pathAfterShapeFunc()
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
          calculations.append("Triangle Base: " + str(triangleBase))
          calculations.append("Triangle Height: " + str(triangleHeight))
          triangleArea = (float(triangleBase) * float(triangleHeight)) / 2
          calculations.append("Triangle Area: " + str(triangleArea))
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
          calculations.append("Triangle Side 1: " + str(triangleSide1))
          calculations.append("Triangle Side 2: " + str(triangleSide2))
          calculations.append("Triangle Side 3: " + str(triangleSide3))
          trianglePerimeter = float(triangleSide1) + float(triangleSide2) + float(triangleSide3)
          calculations.append("Triangle Perimeter: " + str(trianglePerimeter))
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
          # COMMIT 10 - The user can now choose to be directed to inputHistory after the calculations are made. A new "calculations"
          # variable has been made, which stores (appends) each of the user's dimensions inputs for every shape, and these can be
          # seen in a list in inputHistory. "Calculations" also appends all answers summoned after the dimension inputs are made.
          # While the calculations list successfully prints and is bug-free, the UI isn't very user-friendly, which will need to be improved in
          # a later commit.
          calculations.append("Triangle Side 1: " + str(triangleSide1))
          calculations.append("Triangle Side 2: " + str(triangleSide2))
          calculations.append("Triangle Side 3: " + str(triangleSide3))
          calculations.append("Triangle Base: " + str(triangleBase))
          calculations.append("Triangle Height: " + str(triangleHeight))
          triangleArea = (float(triangleBase) * float(triangleHeight)) / 2
          trianglePerimeter = float(triangleSide1) + float(triangleSide2) + float(triangleSide3)
          print("The area of the triangle is: " + str(triangleArea))
          calculations.append("Triangle Area: " + str(triangleArea))
          print("The perimeter of the triangle is: " + str(trianglePerimeter))
          calculations.append("Triangle Perimeter: " + str(trianglePerimeter))

      else:
        print("This is not a valid answer.")
        triangle()

      def pathAfterShapeFunc():
        print()
        print("What do you wish to do now?")
        print()
        print(" - A: Solve another triangle")
        print(" - B: Choose another shape")
        print(" - C: View the history of all your calculations")
        pathAfterShape = input()
        if pathAfterShape == "A" or pathAfterShape == "a":
          triangle()
        elif pathAfterShape == "b" or pathAfterShape == "B":
          main()
        elif pathAfterShape == "c" or pathAfterShape == "C":
          inputHistory()
        else:
          print("This is an invalid response. Please type the letter for your choice.")
          pathAfterShapeFunc()
      pathAfterShapeFunc()
      
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
        calculations.append("Circle Radius: " + str(circleRadius))
        circleArea = math.pi * (float(circleRadius) * float(circleRadius))
        calculations.append("Circle Area: " + str(circleArea))
        circlePerimeter = 2 * math.pi * float(circleRadius)
        calculations.append("Circle Perimeter: " + str(circlePerimeter))
        print("The area of the circle is: " + str(circleArea))
        print("The circumference of the circle is: " + str(circlePerimeter))

      def pathAfterShapeFunc():
        print()
        print("What do you wish to do now?")
        print()
        print(" - A: Solve another circle")
        print(" - B: Choose another shape")
        print(" - C: View the history of all your calculations")
        pathAfterShape = input()
        if pathAfterShape == "A" or pathAfterShape == "a":
          circle()
        elif pathAfterShape == "b" or pathAfterShape == "B":
          main()
        elif pathAfterShape == "c" or pathAfterShape == "C":
          inputHistory()
        else:
          print("This is an invalid response. Please type the letter for your choice.")
          pathAfterShapeFunc()
      pathAfterShapeFunc()
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
          calculations.append("Parallelogram Base: " + str(parallelogramBase))
          calculations.append("Parallelogram Height: " + str(parallelogramHeight))
          parallelogramArea = float(parallelogramBase) * float(parallelogramHeight)
          calculations.append("Parallelogram Area: " + str(parallelogramArea))
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
          calculations.append("Parallelogram Base: " + str(parallelogramBase))
          calculations.append("Parallelogram Side: " + str(parallelogramSide))
          parallelogramPerimeter = 2 * (float(parallelogramSide) + float(parallelogramBase))
          calculations.append("Parallelogram Perimeter: " + str(parallelogramPerimeter))
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
          calculations.append("Parallelogram Base: " + str(parallelogramBase))
          calculations.append("Parallelogram Side: " + str(parallelogramSide))
          calculations.append("Parallelogram Height: " + str(parallelogramHeight))
          parallelogramArea = float(parallelogramBase) * float(parallelogramHeight)
          calculations.append("Parallelogram Area: " + str(parallelogramArea))
          parallelogramPerimeter = 2 * (float(parallelogramSide) + float(parallelogramBase))
          calculations.append("Parallelogram Perimeter: " + str(parallelogramPerimeter))
          print("The area of the parallelogram is: " + str(parallelogramArea))
          print("The perimeter of the parallelogram is: " + str(parallelogramPerimeter))
      else:
        print("This is not a valid answer.")
        parallelogram()

      def pathAfterShapeFunc():
        print()
        print("What do you wish to do now?")
        print()
        print(" - A: Solve another parallelogram")
        print(" - B: Choose another shape")
        print(" - C: View the history of all your calculations")
        pathAfterShape = input()
        if pathAfterShape == "A" or pathAfterShape == "a":
          parallelogram()
        elif pathAfterShape == "b" or pathAfterShape == "B":
          main()
        elif pathAfterShape == "c" or pathAfterShape == "C":
          inputHistory()
        else:
          print("This is an invalid response. Please type the letter for your choice.")
          pathAfterShapeFunc()
      pathAfterShapeFunc()
    parallelogram()
    
    
  else:
    print("This is not a valid shape. Please try again.")
    main()

# COMMIT 10 - The user can now choose to be directed to inputHistory after the calculations are made. A new "calculations"
# variable has been made, which stores (appends) each of the user's dimensions inputs for every shape, and these can be
# seen in a list in inputHistory. "Calculations" also appends all answers summoned after the dimension inputs are made.
# While the calculations list successfully prints and is bug-free, the UI isn't very user-friendly, which will need to be improved in
# a later commit.

calculations = []
def inputHistory():
  print()
  print("All previous calculations:")
  print(calculations)


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