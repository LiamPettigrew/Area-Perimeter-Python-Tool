# Area / Perimeter Python Tool - Created by Liam Pettigrew

# FINAL COMMIT - The program has been thoroughly tested and trialed for any bugs or errors.
# Every path possible for the program has been tested, and no ValueErrors, syntax errors, exceptions,
# typographical errors, etc have been found, for any invalid answers inputted. A few minor parts of
# the code were fixed to make the program more polished, clean, and eliminate any bugs for the final
# product.

# NOTE: Beginning of the code is in line 528.

import math
import os
from colorama import Fore, Back, Style
import time

line = "========================================"

def main():
  # COMMIT 2 - Added the main() shape selection, where the user can choose to select either a
  # rectangle, triangle, circle, or a parallelogram. I have also implemented answer-checkers throughout
  # the code, so that the program responds to invalid answers.
  print()
  print(Fore.CYAN + Style.BRIGHT + "SHAPE SELECTION" + Style.RESET_ALL)
  print("Please enter the shape you are wishing to solve.")
  print()
  print(line)
  print()
  time.sleep(0.05)
  print(" 1) Rectangle")
  time.sleep(0.05)
  print(" 2) Triangle")
  time.sleep(0.05)
  print(" 3) Circle")
  time.sleep(0.05)
  print(" 4) Parallelogram")
  time.sleep(0.05)
  print()
  print(line)
  print()
  whichShape = input(" • Enter (Number): ")
  # COMMIT 3 - Added the dimension selections to every individual shape, which correlates to the
  # properties of the particular shape. Program breaks after dimensions are input.
  if whichShape == "Rectangle" or whichShape == "rectangle" or whichShape == "1":
    os.system("clear")
    def rectangle():
      print(Fore.CYAN + Style.BRIGHT + "RECTANGLE DIMENSION SELECTION" + Style.RESET_ALL)
      print()
      # COMMIT 5 - Added the mathematics functions for the rectangle selection. Now, both the area and perimeter
      # is calculated for the rectangle based on the user's input. Question also returns if the user mistakenly inputs a letter.
      rectangleHeight = input(" • Please enter the height: ")
      rectangleWidth = input(" • Please enter the width: ")
      RHdigit = rectangleHeight.isdigit()
      RWdigit = rectangleWidth.isdigit()
      if RHdigit == False or RWdigit == False:
        os.system("clear")
        print()
        print(Fore.RED + "Your answers need to be in numbers. Please try again." + Style.RESET_ALL)
        print()
        rectangle()
      else:
        rectangleCalculation.append("►► Rectangle height: " + str(rectangleHeight))
        rectangleCalculation.append("►► Rectangle width: " + str(rectangleWidth))
        rectangleArea = float(rectangleHeight) * float(rectangleWidth)
        print()
        rectangleCalculation.append("= Rectangle Area: " + str(rectangleArea))
        rectanglePerimeter = (float(rectangleHeight) + (float(rectangleWidth))) * 2
        rectangleCalculation.append("= Rectangle Perimeter " + str(rectanglePerimeter))
        print(line)
        print()
        print(Style.BRIGHT + "The area of this rectangle is: " + str(rectangleArea) + Style.RESET_ALL)
        print(Style.BRIGHT + "The perimeter of this rectangle is: " + str(rectanglePerimeter) + Style.RESET_ALL)
        print()
        print(line)

        # COMMIT 9 - Added individual path selections for each shape for after the calculations are shown. Once the user is finished, they can now choose
        # to solve another shape for the selected shape they're currently on (looping back to the function of the shape), or
        # choose another shape (returning back to the start of main()). A choice for the history of all calculations made has
        # also been included, however it hasn't been coded yet. The question returns if the user inputs an invalid answer.
        def pathAfterShapeFunc():
          print()
          print("What do you wish to do now?")
          print()
          print(" 1) Solve another rectangle")
          print(" 2) Choose another shape")
          print(" 3) View the history of all your calculations")
          print()
          pathAfterShape = input(" • Enter (Number): ")
          if pathAfterShape == "1":
            os.system("clear")
            rectangle()
          elif pathAfterShape == "2":
            os.system("clear")
            main()
          elif pathAfterShape == "3":
            os.system("clear")
            inputHistory()
          else:
            os.system("clear")
            print(Fore.RED + "This is an invalid response. Please type the letter for your choice." + Style.RESET_ALL)
            pathAfterShapeFunc()
        pathAfterShapeFunc()
    rectangle()
    
  elif whichShape == "Triangle" or whichShape == "triangle" or whichShape == "2":
    os.system("clear")
    def triangle():
      print(Fore.CYAN + Style.BRIGHT + "TRIANGLE DIMENSION SELECTION" + Style.RESET_ALL)
      print()
      print("What do you wish to find out?")
      print()
      print(line)
      print()
      print(" 1) Area")
      print(" 2) Perimeter")
      print(" 3) Both")
      print()
      print(line)
      print()
      triangleSelection = input(" • Enter (Number): ")
      # COMMIT 4 - Added a more advanced triangle dimension selection to make it easier for the user.
      # The user can now select if they are wanting to find out the area, perimeter, or both before entering the calculations.
      # Also returns the question if the user inputted an unknown response.
      if triangleSelection == "Area" or triangleSelection == "area" or triangleSelection == "1":
        os.system("clear")
        print(Fore.CYAN + Style.BRIGHT + "TRIANGLE AREA DIMENSION SELECTION" + Style.RESET_ALL)
        print()
        triangleBase = input(" • Please enter the width of the base: ")
        triangleHeight = input(" • Please enter the length of the height: ")
        # COMMIT 6 - Added mathematical functions to the triangle selection, for the area, perimeter, and both function.
        # Function returns if the user inputs a letter instead of a number.
        THdigit = triangleHeight.isdigit()
        TBdigit = triangleBase.isdigit()
        if THdigit == False or TBdigit == False:
          os.system("clear")
          print()
          print(Fore.RED + "Your answers need to be in numbers. Please try again." + Style.RESET_ALL)
          print()
          triangle()
        else:
          triangleCalculation.append("►► Triangle Base: " + str(triangleBase))
          triangleCalculation.append("►► Triangle Height: " + str(triangleHeight))
          triangleArea = (float(triangleBase) * float(triangleHeight)) / 2
          print()
          triangleCalculation.append("= Triangle Area: " + str(triangleArea))
          print(line)
          print()
          print(Style.BRIGHT + "The area of the triangle is: " + str(triangleArea) + Style.RESET_ALL)
          print()
          print(line)
      elif triangleSelection == "perimeter" or triangleSelection == "Perimeter" or triangleSelection == "2":
        os.system("clear")
        print(Fore.CYAN + Style.BRIGHT + "TRIANGLE PERIMETER DIMENSION SELECTION" + Style.RESET_ALL)
        print()
        triangleSide1 = input(" • Please enter the length of side 1: ")
        triangleSide2 = input(" • Please enter the length of side 2: ")
        triangleSide3 = input(" • Please enter the length of side 3: ")
        TS1digit = triangleSide1.isdigit()
        TS2digit = triangleSide2.isdigit()
        TS3digit = triangleSide3.isdigit()
        if TS1digit == False or TS2digit == False or TS3digit == False:
          os.system("clear")
          print()
          print(Fore.RED + "Your answers need to be in numbers. Please try again." + Style.RESET_ALL)
          print()
          triangle()
        else:
          triangleCalculation.append("►► Triangle Side 1: " + str(triangleSide1))
          triangleCalculation.append("►► Triangle Side 2: " + str(triangleSide2))
          triangleCalculation.append("►► Triangle Side 3: " + str(triangleSide3))
          trianglePerimeter = float(triangleSide1) + float(triangleSide2) + float(triangleSide3)
          triangleCalculation.append("= Triangle Perimeter: " + str(trianglePerimeter))
          print()
          print(line)
          print()
          print(Style.BRIGHT + "The perimeter of the triangle is: " + str(trianglePerimeter) + Style.RESET_ALL)
          print()
          print(line)
      elif triangleSelection == "both" or triangleSelection == "Both" or triangleSelection == "3":
        os.system("clear")
        print(Fore.CYAN + Style.BRIGHT + "TRIANGLE AREA & PERIMETER DIMENSION SELECTION" + Style.RESET_ALL)
        print()
        triangleSide1 = input(" • Please enter the length of side 1: ")
        triangleSide2 = input(" • Please enter the length of side 2: ")
        triangleSide3 = input(" • Please enter the length of side 3: ")
        triangleBase = input(" • Please enter the width of the base: ")
        triangleHeight = input(" • Please enter the length of the height: ")
        TS1digit = triangleSide1.isdigit()
        TS2digit = triangleSide2.isdigit()
        TS3digit = triangleSide3.isdigit()
        THdigit = triangleHeight.isdigit()
        TBdigit = triangleBase.isdigit()
        if TS1digit == False or TS2digit == False or TS3digit == False or THdigit == False or TBdigit == False:
          os.system("clear")
          print()
          print(Fore.RED + "Your answers need to be in numbers. Please try again." + Style.RESET_ALL)
          print()
          triangle()
        else:
          # COMMIT 10 - The user can now choose to be directed to inputHistory after the calculations are made. A new "calculations"
          # variable has been made, which stores (appends) each of the user's dimensions inputs for every shape, and these can be
          # seen in a list in inputHistory. "Calculations" also appends all answers summoned after the dimension inputs are made.
          # While the calculations list successfully prints and is bug-free, the UI isn't very user-friendly, which will need to be improved in
          # a later commit.
          triangleCalculation.append("►► Triangle Side 1: " + str(triangleSide1))
          triangleCalculation.append("►► Triangle Side 2: " + str(triangleSide2))
          triangleCalculation.append("►► Triangle Side 3: " + str(triangleSide3))
          triangleCalculation.append("►► Triangle Base: " + str(triangleBase))
          triangleCalculation.append("►► Triangle Height: " + str(triangleHeight))
          triangleArea = (float(triangleBase) * float(triangleHeight)) / 2
          trianglePerimeter = float(triangleSide1) + float(triangleSide2) + float(triangleSide3)
          print()
          print(line)
          print()
          print(Style.BRIGHT + "The area of the triangle is: " + str(triangleArea) + Style.RESET_ALL)
          triangleCalculation.append("= Triangle Area: " + str(triangleArea))
          print(Style.BRIGHT + "The perimeter of the triangle is: " + str(trianglePerimeter) + Style.RESET_ALL)
          print()
          print(line)
          triangleCalculation.append("= Triangle Perimeter: " + str(trianglePerimeter))

      else:
        os.system("clear")
        print(Fore.RED + "This is not a valid answer." + Style.RESET_ALL)
        triangle()

      def pathAfterShapeFunc():
        print()
        print("What do you wish to do now?")
        print()
        print(" 1) Solve another triangle")
        print(" 2) Choose another shape")
        print(" 3) View the history of all your calculations")
        print()
        pathAfterShape = input(" • Enter (Number): ")
        if pathAfterShape == "1":
          os.system("clear")
          triangle()
        elif pathAfterShape == "2":
          os.system("clear")
          main()
        elif pathAfterShape == "3":
          os.system("clear")
          inputHistory()
        else:
          os.system("clear")
          print(Fore.RED + "This is an invalid response. Please type the letter for your choice." + Style.RESET_ALL)
          pathAfterShapeFunc()
      pathAfterShapeFunc()
      
    triangle()
      
    
  elif whichShape == "Circle" or whichShape == "circle" or whichShape == "3":
    os.system("clear")
    def circle():
      print(Style.BRIGHT + Fore.CYAN + "CIRCLE DIMENSION SELECTION" + Style.RESET_ALL)
      print()
      # COMMIT 7 - The circle mathematical functions have been inputted, which calculates both the area and
      # circumference of the circle, using the "math.pi" imported tool. Question returns if user mistakenly
      # inputs a letter instead of a number.
      circleRadius = input(" • Please enter the radius: ")
      CRdigit = circleRadius.isdigit()
      if CRdigit == False:
        os.system("clear")
        print()
        print(Fore.RED + "Your answers need to be in numbers. Please try again." + Style.RESET_ALL)
        print()
        circle()
      else:
        circleCalculation.append("►► Circle Radius: " + str(circleRadius))
        circleArea = math.pi * (float(circleRadius) * float(circleRadius))
        circleCalculation.append("= Circle Area: " + str(circleArea))
        circlePerimeter = 2 * math.pi * float(circleRadius)
        circleCalculation.append("= Circle Perimeter: " + str(circlePerimeter))
        print()
        print(line)
        print()
        print(Style.BRIGHT + "The area of the circle is: " + str(circleArea) + Style.RESET_ALL)
        print(Style.BRIGHT + "The circumference of the circle is: " + str(circlePerimeter) + Style.RESET_ALL)
        print()
        print(line)

      def pathAfterShapeFunc():
        print()
        print("What do you wish to do now?")
        print()
        print(" 1) Solve another circle")
        print(" 2) Choose another shape")
        print(" 3) View the history of all your calculations")
        print()
        pathAfterShape = input(" • Enter (Number): ")
        if pathAfterShape == "1":
          os.system("clear")
          circle()
        elif pathAfterShape == "2":
          os.system("clear")
          main()
        elif pathAfterShape == "3":
          os.system("clear")
          inputHistory()
        else:
          os.system("clear")
          print(Fore.RED + "This is an invalid response. Please type the letter for your choice." + Style.RESET_ALL)
          pathAfterShapeFunc()
      pathAfterShapeFunc()
    circle()
    
  elif whichShape == "Parallelogram" or whichShape == "parallelogram" or whichShape == "4":
    os.system("clear")
    def parallelogram():
      print(Fore.CYAN + Style.BRIGHT + "PARALLELOGRAM DIMENSION SELECTION" + Style.RESET_ALL)
      print()
      print("What do you wish to find out?")
      print()
      print(line)
      print()
      print(" 1) Area")
      print(" 2) Perimeter")
      print(" 3) Both")
      print()
      print(line)
      print()
      parallelogramSelection = input(" • Enter (Number): ")
      # COMMIT 4 - Added a more advanced parallelogram dimension selection to make it easier for the user.
      # The user can now select if they are wanting to find out the area, perimeter, or both before entering the calculations.
      # Also returns the question if the user inputted an unknown response.
      if parallelogramSelection == "Area" or parallelogramSelection == "area" or parallelogramSelection == "1":
        os.system("clear")
        print(Fore.CYAN + Style.BRIGHT + "PARALLELOGRAM AREA DIMENSION SELECTION" + Style.RESET_ALL)
        print()
        parallelogramBase = input(" • Please enter the width of the base: ")
        parallelogramHeight = input(" • Please enter the length of the height: ")
        # COMMIT 8 - Added the mathematical functions for the parallelogram (for the area, perimeter, and both). Question
        # returns if the user inputs an invalid response. This concludes Phase Three, now that all mathematical functions
        # have been put in. However, after calculating each question, the program breaks.
        PBdigit = parallelogramBase.isdigit()
        PHdigit = parallelogramHeight.isdigit()
        if PBdigit == False or PHdigit == False:
          os.system("clear")
          print()
          print(Fore.RED + "Your answers need to be in numbers. Please try again." + Style.RESET_ALL)
          print()
          parallelogram()
        else:
          parallelogramCalculation.append("►► Parallelogram Base: " + str(parallelogramBase))
          parallelogramCalculation.append("►► Parallelogram Height: " + str(parallelogramHeight))
          parallelogramArea = float(parallelogramBase) * float(parallelogramHeight)
          print()
          print(line)
          print()
          parallelogramCalculation.append("= Parallelogram Area: " + str(parallelogramArea))
          print(Style.BRIGHT + "The area of the parallelogram is: " + str(parallelogramArea) + Style.RESET_ALL)
          print()
          print(line)
      elif parallelogramSelection == "perimeter" or parallelogramSelection == "Perimeter" or parallelogramSelection == "2":
        os.system("clear")
        print(Fore.CYAN + Style.BRIGHT + "PARALLELOGRAM PERIMETER DIMENSION SELECTION" + Style.RESET_ALL)
        print()
        parallelogramSide = input(" • Please enter the length of the side: ")
        parallelogramBase = input(" • Please enter the width of the base: ")
        PSdigit = parallelogramSide.isdigit()
        PBdigit = parallelogramBase.isdigit()
        if PSdigit == False or PBdigit == False:
          os.system("clear")
          print()
          print(Fore.RED + "Your answers need to be in numbers. Please try again." + Style.RESET_ALL)
          print()
          parallelogram()
        else:
          parallelogramCalculation.append("►► Parallelogram Base: " + str(parallelogramBase))
          parallelogramCalculation.append("►► Parallelogram Side: " + str(parallelogramSide))
          parallelogramPerimeter = 2 * (float(parallelogramSide) + float(parallelogramBase))
          print()
          print(line)
          print()
          parallelogramCalculation.append("= Parallelogram Perimeter: " + str(parallelogramPerimeter))
          print(Style.BRIGHT + "The perimeter of the parallelogram is: " + str(parallelogramPerimeter) + Style.RESET_ALL)
          print()
          print(line)
      elif parallelogramSelection == "Both" or parallelogramSelection == "both" or parallelogramSelection == "3":
        os.system("clear")
        print(Fore.CYAN + Style.BRIGHT + "PARALLELOGRAM AREA & PERIMETER DIMENSION SELECTION" + Style.RESET_ALL)
        print()
        parallelogramSide = input(" • Please enter the length of the side: ")
        parallelogramBase = input(" • Please enter the width of the base: ")
        parallelogramHeight = input(" • Please enter the length of the height: ")
        PSdigit = parallelogramSide.isdigit()
        PBdigit = parallelogramBase.isdigit()
        PHdigit = parallelogramHeight.isdigit()
        if PBdigit == False or PHdigit == False or PSdigit == False:
          os.system("clear")
          print()
          print(Fore.RED + "Your answers need to be in numbers. Please try again." + Style.RESET_ALL)
          print()
          parallelogram()
        else:
          parallelogramCalculation.append("►► Parallelogram Side: " + str(parallelogramSide))
          parallelogramCalculation.append("►► Parallelogram Base: " + str(parallelogramBase))
          parallelogramCalculation.append("►► Parallelogram Height: " + str(parallelogramHeight))
          parallelogramArea = float(parallelogramBase) * float(parallelogramHeight)
          print()
          parallelogramCalculation.append("= Parallelogram Area: " + str(parallelogramArea))
          parallelogramPerimeter = 2 * (float(parallelogramSide) + float(parallelogramBase))
          parallelogramCalculation.append("= Parallelogram Perimeter: " + str(parallelogramPerimeter))
          print(line)
          print()
          print(Style.BRIGHT + "The area of the parallelogram is: " + str(parallelogramArea) + Style.RESET_ALL)
          print(Style.BRIGHT + "The perimeter of the parallelogram is: " + str(parallelogramPerimeter) + Style.RESET_ALL)
          print()
          print(line)
      else:
        os.system("clear")
        print(Fore.RED + "This is not a valid answer." + Style.RESET_ALL)
        parallelogram()

      def pathAfterShapeFunc():
        print()
        print("What do you wish to do now?")
        print()
        print(" 1) Solve another parallelogram")
        print(" 2) Choose another shape")
        print(" 3) View the history of all your calculations")
        print()
        pathAfterShape = input("Enter (Number): ")
        if pathAfterShape == "1":
          os.system("clear")
          parallelogram()
        elif pathAfterShape == "2":
          os.system("clear")
          main()
        elif pathAfterShape == "3":
          os.system("clear")
          inputHistory()
        else:
          os.system("clear")
          print(Fore.RED + "This is an invalid response. Please type the letter for your choice." + Style.RESET_ALL)
          pathAfterShapeFunc()
      pathAfterShapeFunc()
    parallelogram()
    
    
  else:
    os.system("clear")
    print(Fore.RED + "This is not a valid shape. Please try again." + Style.RESET_ALL)
    main()

# COMMIT 10 - The user can now choose to be directed to inputHistory after the calculations are made. A new "calculations"
# variable has been made, which stores (appends) each of the user's dimensions inputs for every shape, and these can be
# seen in a list in inputHistory. "Calculations" also appends all answers summoned after the dimension inputs are made.
# While the calculations list successfully prints and is bug-free, the UI isn't very user-friendly, which will need to be improved in
# a later commit.

# COMMIT 11 - Changed the UI of the calculations history log into a tidy, vertical list, with all of the inputs and
# calculations separated between gaps. I achieved this by having calculation lists for every shape individually, instead
# of having one "calculations" variable. This makes every shape's inputs and calculations categorized. I have tested and made sure
# this new code is bug-free.

rectangleCalculation = []
triangleCalculation = []
circleCalculation = []
parallelogramCalculation = []

def inputHistory():
  os.system("clear")
  print()
  print(Style.BRIGHT + Fore.CYAN + "ALL PREVIOUS CALCULATIONS" + Style.RESET_ALL)
  print()
  print(line)
  print()
  # FINAL COMMIT - Tidied up the calculation history by implementing "lens".
  if len(rectangleCalculation) > 1:
    print("RECTANGLE:")
    for gap1 in rectangleCalculation:
      time.sleep(0.05)
      print(gap1)
  if len(triangleCalculation):
    print()
    print("TRIANGLE:")
    for gap2 in triangleCalculation:
      time.sleep(0.05)
      print(gap2)
  if len(circleCalculation):
    print()
    print("CIRCLE:")
    for gap3 in circleCalculation:
      time.sleep(0.05)
      print(gap3)
  if len(parallelogramCalculation):
    print()
    print("PARALLELOGRAM:")
    for gap4 in parallelogramCalculation:
      time.sleep(0.05)
      print(gap4)
  print()
  print(line)
  print()
  # COMMIT 12 - Added the final component to Phase Five. After the calculation history is shown, the user can now
  # return back to the shape selection by pressing enter. The question returns if the user inputs an invalid answer.
  # This now completed the necessities of the program, as the program now does not have an end, and fully loops.
  # Extensive bug-testing for every possible outcome has taken place for this code, and no bugs, glitches or errors
  # have been found.
  def afterHistoryLoop():
    print()
    enterAfterHistory = input(" • Press <enter> to return to the shape selection: ")
    if enterAfterHistory == (""):
      os.system("clear")
      main()
    else:
      print(Fore.RED + "This is not a valid answer." + Style.RESET_ALL)
      afterHistoryLoop()
  afterHistoryLoop()


# COMMIT 1 - Added copyright information and welcome message.
# Asks the user if they wish to either continue to the shape selection (main) or view the instructions.
# If the user wishes to view the instructions, the program shows a list of information about the program.
# Once the user finishes with the instructions, they are able to continue to main.

# COMMIT 14 - Majorly improved the UI of the program, to make it more user-friendly, easy to use, and accessible.
# I achieved this by adding colours to to program using "colorama" to distinguish titles with instructions, options, information, etc.
# I also added lines to separate options and instructions with commands, as well as bullet points to signal where to type.
# Some of the code has also be changed from a worded or lettered response to a simpler numbered system, where the user can simply
# Type the number of their choice. E.g. Before, the user had to type either "instructions" or "continue" at the start of the
# program, whereas now, they can simply type "1" or "2". This number system is now consistent throughout the program, replacing
# "a, b, c" options with "1, 2, 3". The calculation history screen has also had a big UI change to make it more easily understandable.
# Time.Sleeps have also been implemented for style reasons.

print(Style.DIM + "Ⓒ Area & Perimeter Calculator Tool Python Program created and authorised by Liam Pettigrew for personal and educational use.")
print("Ⓒ All program code was written, implemented, and rightfully belong to Liam Pettigrew, the creator of the program.")
print("Ⓒ Program first created in July 2022 for Fraser High School." + Style.RESET_ALL)
print()
print(Fore.CYAN + Style.BRIGHT + "\nWelcome to the Area & Perimeter Calculator Tool." + Style.RESET_ALL)
def start():
  print("Do you wish to view the instructions to the program or continue to the shape selection?")
  print()
  print(line)
  print()
  print(" 1) Instructions")
  print(" 2) Continue")
  print()
  print(line)
  print()
  instructionsOrContinue = input(" • Enter (Number): ")
    
  if instructionsOrContinue == "continue" or instructionsOrContinue == "Continue" or instructionsOrContinue == "2":
    # COMMIT 13 - Added the "system" plugin. The code now clears the screen after every input to keep it looking tidy.
    os.system("clear")
    # MAIN() IS AT LINE 16
    main()
  
  elif instructionsOrContinue == "instructions" or instructionsOrContinue == "Instructions" or instructionsOrContinue == "1":
    os.system("clear")
    # COMMIT 15 - Updated and improved the program instructions. It now has more information and instructions.
    print()
    print(Fore.CYAN + Style.BRIGHT + "PROGRAM INSTRUCTIONS" + Style.RESET_ALL)
    print()
    print(line)
    print()
    print("The Area & Perimeter Calculator Tool, created by Liam Pettigrew, is an easy-to-use way for students to check their mathematics work.")
    print("The program offers a list of shapes to choose from:")
    print(" • Rectangle")
    print(" • Triangle")
    print(" • Circle")
    print(" • Parallelogram")
    print()
    print("For any of these shapes chosen, the program will ask for all the known dimensions. The program will then solve the area and perimeter for the shape (in any metric they wish, as long as it is used consistantly.")
    print("The user can then choose to solve another shape, for as many times as they wish. The program is easy-to-use, so very little pathways are needed in the code to loop back and select another shape.")
    print("When exiting the code, the user is able to view the history of all of their calculations made while the program was running.")
    print()
    print("This program was intended for use of Fraser High School students. Enjoy your time using this program!")
    print()
    print(line)
    print()
    print("Are you ready to continue to the shape selection?")
    print()
    def afterInstructionsLoop():
      print(" • Press <enter>")
      continueAfterInstructions = input()
      if continueAfterInstructions == (""):
        os.system("clear")
        # MAIN() IS AT LINE 16
        main()
      else:
        print(Fore.RED + "This is not a valid answer." + Style.RESET_ALL)
        afterInstructionsLoop()
    afterInstructionsLoop()
  
  else:
    os.system("clear")
    print()
    print(Fore.RED + "This is not a valid response. Please try again." + Style.RESET_ALL)
    print()
    start()

# START TO THE CODE
start()