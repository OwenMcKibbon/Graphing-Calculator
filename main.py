#These are the imported softwares and whatnot that we used.
import easygui
from easygui import *

import numpy as np
import pylab as pl

import os
import tempfile

os.environ["MPLCONFIGDIR"] = tempfile.gettempdir()
import matplotlib.pyplot as plt

#I put the images up here and defined them, just to avoid annoyances with them down the line.

logoScreen = 'Logo-Screen.png'
graphButton = 'Graph-Button.png'
menuScreen = 'Menu-Screen.png'
placeholderScreen = 'Placeholder-Screen.png'
GR9TScreen = 'GR9T-Screen.png'
GR10TScreen = 'GR10T-Screen.png'
GR11TScreen = 'GR11T-Screen.png'
GR12TScreen = 'GR12T-Screen.png'
GR9EScreen = 'GR9E-Screen.png'
GR10EScreen = 'GR10E-Screen.png'
GR11EScreen = 'GR11E-Screen.png'
GR12EScreen = 'GR12E-Screen.png'

#The lists below have the button options for the main menu screen and home screen.

activation = ["C O N T I N U E"]
menuOptions = [
    "Grade 9\nTextbook", "Grade 10\nTextbook", "Grade 11\nTextbook",
    "Grade 12\nTextbook", "Grade 9\nEquations", "Grade 10\nEquations",
    "Grade 11\nEquations", "Grade 12\nEquations"
]
#These are the test questions. Seeing how they weren't the highest priority, they are not all filled out.
test001Q1 = ["", "", "", ""]
test001Q2 = ["", "", "", ""]
test001Q3 = ["", "", "", ""]
test001Q4 = ["", "", "", ""]
test001Q5 = ["", "", "", ""]
test001Q6 = ["", "", "", ""]
test001Q7 = ["", "", "", ""]
test001Q8 = ["", "", "", ""]
test001Q9 = ["", "", "", ""]
test001Q10 = ["", "", "", ""]
test002Q1 = ["", "", "", ""]
test002Q2 = ["", "", "", ""]
test002Q3 = ["", "", "", ""]
test002Q4 = ["", "", "", ""]
test002Q5 = ["", "", "", ""]
test002Q6 = ["", "", "", ""]
test002Q7 = ["", "", "", ""]
test002Q8 = ["", "", "", ""]
test002Q9 = ["", "", "", ""]
test002Q10 = ["", "", "", ""]
test003Q1 = [
    "Reciprocal Function", "Cubic Function", "Square Root Function",
    "Absolute Value Function"
]
test003Q2 = ["True", "False"]
test003Q3 = ["4", "9", "7", "0"]
test003Q4 = [
    "The height of a\nlinear function.",
    "Whether or not something\nis a function.",
    "The distance between\ntwo points.",
    "Whether or not the\nline is on an angle."
]
test003Q5 = [
    "Square Root Function", "Cube Root Function", "Quadratic Function",
    "Cubic Function"
]
test003Q6 = ["-3, -24, -81", "3, 12, 27", "3, 24, 81", "-3, -12, -27"]
test003Q7 = ["", "", "", ""]
test003Q8 = ["", "", "", ""]
test003Q9 = ["", "", "", ""]
test003Q10 = ["", "", "", ""]
test004Q1 = ["", "", "", ""]
test004Q2 = ["", "", "", ""]
test004Q3 = ["", "", "", ""]
test004Q4 = ["", "", "", ""]
test004Q5 = ["", "", "", ""]
test004Q6 = ["", "", "", ""]
test004Q7 = ["", "", "", ""]
test004Q8 = ["", "", "", ""]
test004Q9 = ["", "", "", ""]
test004Q10 = ["", "", "", ""]
test005Q1 = ["", "", "", ""]
test005Q2 = ["", "", "", ""]
test005Q3 = ["", "", "", ""]
test005Q4 = ["", "", "", ""]
test005Q5 = ["", "", "", ""]
test005Q6 = ["", "", "", ""]
test005Q7 = ["", "", "", ""]
test005Q8 = ["", "", "", ""]
test005Q9 = ["", "", "", ""]
test005Q10 = ["", "", "", ""]
test006Q1 = ["", "", "", ""]
test006Q2 = ["", "", "", ""]
test006Q3 = ["", "", "", ""]
test006Q4 = ["", "", "", ""]
test006Q5 = ["", "", "", ""]
test006Q6 = ["", "", "", ""]
test006Q7 = ["", "", "", ""]
test006Q8 = ["", "", "", ""]
test006Q9 = ["", "", "", ""]
test006Q10 = ["", "", "", ""]
test007Q1 = ["", "", "", ""]
test007Q2 = ["", "", "", ""]
test007Q3 = ["", "", "", ""]
test007Q4 = ["", "", "", ""]
test007Q5 = ["", "", "", ""]
test007Q6 = ["", "", "", ""]
test007Q7 = ["", "", "", ""]
test007Q8 = ["", "", "", ""]
test007Q9 = ["", "", "", ""]
test007Q10 = ["", "", "", ""]
test008Q1 = ["", "", "", ""]
test008Q2 = ["", "", "", ""]
test008Q3 = ["", "", "", ""]
test008Q4 = ["", "", "", ""]
test008Q5 = ["", "", "", ""]
test008Q6 = ["", "", "", ""]
test008Q7 = ["", "", "", ""]
test008Q8 = ["", "", "", ""]
test008Q9 = ["", "", "", ""]
test008Q10 = ["", "", "", ""]

#For the sake of having it be more neat (and more professional), I decided to assign each lesson an index number. They will be seen below.
GR9Toptions = ["Basic Polynomials", "Linear Relations", "RETURN TO MENU"]
#Basic Polynomials - 001
#Linear Relations - 002
GR10Toptions = ["Quadratics", "Analytic Geometry", "RETURN TO MENU"]
#Quadratics - 003
#Analytic Geometry - 004
GR11Toptions = [
    "Different Kinds\nof Functions", "Trigonometry", "RETURN TO MENU"
]
#Different Types of Functions - 005
#Trigonometry - 006
GR12Toptions = ["OPTION 1", "OPTION 2", "RETURN TO MENU"]
#PLACEHOLDER - 007
#PLACEHOLDER - 008
GR9Eoptions = [
    "Basic Polynomials\nPRACTICE", "Linear Relations\nPRACTICE",
    "Basic Polynomials\nTEST", "Linear Relations\nTEST", "RETURN TO MENU"
]
#Basic Polynomials (Practice) - 001
#Linear Relations (Practice) - 002
#Basic Polynomials (Test) - 001
#Linear Relations (Test) - 002
GR10Eoptions = [
    "Quadratics\nPRACTICE", "Analytic Geometry\nPRACTICE", "Quadratics\nTEST",
    "Analytic Geometry\nTEST", "RETURN TO MENU"
]
#Quadratics (Practice) - 003
#Analytic Geometry (Practice) - 004
#Quadratics (Test) - 003
#Analytic Geometry (Test) - 004
GR11Eoptions = [
    "Different Kinds\nof Functions\nPRACTICE", "Trigonometry\nPRACTICE",
    "Different Kinds\nof Functions\nTEST", "Trigonometry\nTEST",
    "RETURN TO MENU"
]
#Different Types of Functions (Practice) - 005
#Trigonometry (Practice) - 006
#Different Types of Functions (Test) - 005
#Trigonometry (Test) - 006
GR12Eoptions = [
    "SUBJECT 1\nPRACTICE", "SUBJECT 2\nPRACTICE", "SUBJECT 1\nTEST",
    "SUBJECT 2\nTEST", "RETURN TO MENU"
]
#PLACEHOLDER (Practice) - 007
#PLACEHOLDER (Practice) - 008
#PLACEHOLDER (Test) - 007
#PLACEHOLDER (Test) - 008
placeholderButtons = ["OPTION 1", "RETURN TO MENU"]

#These buttons solely serve the purpose of returning from an unfinished section. Pay it no regard.


#Defining the functions that will call the lessons. Each of these are just text boxes that appear in succession to each other.
def lesson001():  #<---POLYNOMIALS LESSON
    message = ("This is a tutorial on how to deal with basic polynomials.")
    title = ("Basic Polynomials - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "Polynomials are algebraic expressions with coefficients and variables."
    )
    title = ("Basic Polynomials - 2")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "A variable is a value that has values that constantly vary. It is usually represented by a letter."
    )
    title = ("Basic Polynomials - 3")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "A coefficient is a number in an equation that has a set value, but can be modified by the variables."
    )
    title = ("Basic Polynomials - 4")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "A constant is a number in an equation that has a no attached variable, meaning that it's value is constant, hence the name."
    )
    title = ("Basic Polynomials - 5")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "In the equation 3x² + 4y + 7, we see that the coefficients are 5 and 2, being modified by the variables x and y respectively. There is also a constant of 3 at the end. Say that x is equal to 2 and y is equal to 3. What will the solution be?"
    )
    title = ("Basic Polynomials - 6")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "We'll deal with this one step at a time, using BEDMAS. We'll start off by replacing the variables with the values in brackets. This will leave us with 3(2)² x 4(3) + 7."
    )
    title = ("Basic Polynomials - 7")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "First off, we'll deal with the exponent. This will leave us with the following: 12 x 12 + 7"
    )
    title = ("Basic Polynomials - 8")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "Next order of business is dealing with the brackets. 3 x 4 is 12, and 4 x 3 is 12, so the equation will look like this: 12 x 12 + 7."
    )
    title = ("Basic Polynomials - 9")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "Finally, we go left to right. 12 x 12 = 144, and 144 + 7 is equal to 151."
    )
    title = ("Basic Polynomials - 10")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "And voila, we have our answer of 151. Now you (hopefully) have a grasp on how to deal with 3 term polynomials like the one we just dealt with."
    )
    title = ("Basic Polynomials - 11")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = ("You will now be returned to the main menu.")
    title = ("Basic Polynomials - 12")
    menu()


def lesson002():  #<---LINEAR EQUATION LESSON
    message = ("This is a tutorial on how to deal with linear relations.")
    title = ("Linear Relations - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "A linear relation is the relationship between two points on an axis.")
    title = ("Linear Relations - 2")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "Take note of the following equation:\n\ny = mx + b\n\nFamiliarize yourself with this equation. You'll see it quite often."
    )
    title = ("Linear Relations - 3")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "Let's deconstruct this equation one aspect at a time.\nThe y value determines the height of the line.\nThe x value determines the width of the line.\nThe m represents how steep the line is.\nThe b represents the y intercept."
    )
    title = ("Linear Relations - 4")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = ("So, let's start with an equation like so;\n\ny = 2x + 5.")
    title = ("Linear Relations - 5")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "The steepness would be 2, and the y intercept would be 5.\nWith that knowledge, we can gather the following information:\n\n-Since the y intercept is 5, we can say that one of the points is (0,5)\n-The x value will either increase or decrease by 1.\n-The y value will increase or decrease by 2."
    )
    title = ("Linear Relations - 6")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "Using all of that information, we can tell that the line will go through the following points.\n\n-(-4, 3)\n-(-2, 4)\n-(0, 5)\n-(2, 6)"
    )
    title = ("Linear Relations - 7")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "And voila; that is how you deal with linear relations. Hopefully, you will have a better understanding of this subject. You will now be returned to the main menu."
    )
    title = ("Linear Relations - 8")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def lesson003():  #<---QUADRATIC LESSON
    message = ("This is a tutorial on how to deal with quadratics.")
    title = ("Quadratics - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "When dealing with quadratic equations, one thing to note is that there are three different types of equations:\n\n-Standard form -> ax² + bx + c = 0\n-Factored form -> y = a(x - r1)(x - r2)\n-Vertex form -> y = a(x - h)² + k"
    )
    title = ("Quadratics - 2")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "Each form of equation gives you different information from the others:\n\n-Standard form -> End behaviours, values of a,b and c.\n-Factored form -> End behaviours, zeros(x intercepts)\n-Vertex form -> End behaviours, vertex (starting point)"
    )
    title = ("Quadratics - 3")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = ("Starting with standard form, ")
    title = ("Quadratics - 4")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def lesson004():  #<---ANALYTIC GEOMETRY LESSON
    message = ("This is a tutorial on how to deal with analytic geometry.")
    title = ("Analytic Geometry - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def lesson005():  #<---FUNCTIONS LESSON
    message = (
        "This is a tutorial on how to deal with the different assortment of funyuns."
    )
    title = ("Functions - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = ("I meant functions.")
    title = ("Functions - 2")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "There are a large variety of functions. You will be learning about each different one."
    )
    title = ("Functions - 3")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "Starting with the simplest one; the linear. The linear function is a simple straight line (figures)."
    )
    title = ("Functions - 4")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "The equation for a linear equation looks like this:\nf(x) = x.")
    title = ("Functions - 5")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "Following that, we'll be looking at an absolute value function. The absolute value function mirrors itself over the y axis."
    )
    title = ("Functions - 6")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "The equation for an absolute value function looks like this:\nf(x) = |x|"
    )
    title = ("Functions - 7")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = ("Next up, we have the quadratic function. Say hi.")
    title = ("Functions - 8")
    contButton = ("Good day to you.")
    output = msgbox(message, title, contButton)
    message = (
        "It appreciated that! Anyways, the quadratic function (or a parabola) looks like an arc."
    )
    title = ("Functions - 9")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "The direction that the parabola opens is dependant on it's position. If it's above the x axis, the parabola will open downwards, meaning that the branches of the parabola will intersect at the highest point. The opposite rings true if the parabola is below the x axis; it will open upwards and the branches will intersect at the lowest point."
    )
    title = ("Functions - 10")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "Quadratic functions will increase by the square. For instance, if x = 1, it will increase as follows; 1 -> 4 -> 9 -> 16 -> etc."
    )
    title = ("Functions - 11")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "Note that the square will be multiplied by the coefficient. Say for instance, if the coefficient is 3, it will increase in such a matter; 3 -> 12 -> 27 -> 48 -> etc."
    )
    title = ("Functions - 12")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = ("The equation for a parabola looks like this:\nf(x) = x²")
    title = ("Functions - 13")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = ("After that, we have the cubic function.")
    title = ("Functions - 14")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "A cubic function is similar to a quadratic, but with one key difference; one of the branches is going in the opposite direction."
    )
    title = ("Functions - 15")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "In a similar vein to how the quadratic increases, the cubic functions will increase by the cube. For instance, if x = 1, it will increase as follows; 1 -> 8 -> 27 -> 64 -> etc."
    )
    title = ("Functions - 16")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "The same rule with the coefficient applies here, but the number will be cubed. Say for instance, if the coefficient is 2, it will increase in such a matter; 2 -> 16 -> 54 -> 128 -> etc."
    )
    title = ("Functions - 17")
    contButton = ("Continue.")
    message = ("The equation for a cubic looks like this:\nf(x) = x³")
    title = ("Functions - 18")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = ("Here we have the square root function.")
    title = ("Functions - 19")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "One way to look at the square root function is that it's a parabola on its side and with only one branch."
    )
    title = ("Functions - 20")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "The x's value is the y value squared (unless modified). For instance, should the y value equal 2, the x would equal 4, and should the y value equal 4, the x would be 16, and so on and so forth."
    )
    title = ("Functions - 21")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "The equation for a square root function will look something like this:\nf(x) = √x"
    )
    title = ("Functions - 22")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = ("Next stop is the cube root function.")
    title = ("Functions - 23")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "The cube root function works similarily to the cubic function, except like the square root function, it's on its side. However, unlike the square root function, both branches are there. That's because negative cubes are negative, whereas negative squares are positive."
    )
    title = ("Functions - 24")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "As you'd assume, the x value (in its base form) will scale based on the y value. If y is equal to 2, x will be equal to 8, or should y equal -3, x would equal -27."
    )
    title = ("Functions - 25")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "The equation for a cube root function will look something like this:\nf(x) = ³√x"
    )
    title = ("Functions - 26")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = ("This is the last one. Next up is the reciprocal function.")
    title = ("Functions - 27")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "The reciprocal function is a function that mirrors itself over the x and y axis (in its base form)."
    )
    title = ("Functions - 28")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "However, there are limitations, as they can't touch the asymptotes. They can get closer and closer, but they cannot touch them. While in its base form, the asymptotes are the axis themselves."
    )
    title = ("Functions - 29")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "The equation for a reciprocal function would look like this:\nf(x) = 1/x"
    )
    title = ("Functions - 30")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "One last thing to note about a function is that if a y has 2 x's, it can't be a function."
    )
    title = ("Functions - 31")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    message = (
        "Well, that took a while. You should (hopefully) have a better understanding of the different array of functions. And now, back to the menu."
    )
    title = ("Functions - 32")
    contButton = ("Continue.")
    output = msgbox(message, title, contButton)
    menu()


def lesson006():  #<---TRIGONOMETRY LESSON
    message = ("This is a tutorial on how to deal with trigonometry.")
    title = ("Trigonometry - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "Trigonometry tackles the lengths and angles of triangles. We'll be discussing sine, cosine and tangent and all of that noise."
    )
    title = ("Trigonometry - 2")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = ("Trigonometry tackles the lengths and angles of triangles.")
    title = ("Trigonometry - 3")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def lesson007():  #<---TRIGONOMETRY LESSON
    message = ("This is a placeholder tutorial. Pay it no regard.")
    title = ("Placeholder - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def lesson008():  #<---TRIGONOMETRY LESSON
    message = ("This is a placeholder tutorial. Pay it no regard.")
    title = ("Placeholder - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


#The practice sections will have practice questions to help the user understand these concepts.
def practice001():
    message = ("This is a placeholder tutorial. Pay it no regard.")
    title = ("Placeholder - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def practice002():
    message = ("This is a placeholder tutorial. Pay it no regard.")
    title = ("Placeholder - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def practice003():
    message = ("This is a placeholder tutorial. Pay it no regard.")
    title = ("Placeholder - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def practice004():
    message = ("This is a placeholder tutorial. Pay it no regard.")
    title = ("Placeholder - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def practice005():
    message = ("This is a placeholder tutorial. Pay it no regard.")
    title = ("Placeholder - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def practice006():
    message = ("This is a placeholder tutorial. Pay it no regard.")
    title = ("Placeholder - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def practice007():
    message = ("This is a placeholder tutorial. Pay it no regard.")
    title = ("Placeholder - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def practice008():
    message = ("This is a placeholder tutorial. Pay it no regard.")
    title = ("Placeholder - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


#The tests will help test the knowledge of the user.
def test001():
    message = ("This test will challenge your skills on polynomials.")
    title = ("Polynomials Test - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = ("There are 10 multiple choice questions. Good luck!")
    title = ("Polynomials Test - 2")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def test002():
    message = ("This test will challenge your skills on linear relations.")
    title = ("Linear Relations Test - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = ("There are 10 multiple choice questions. Good luck!")
    title = ("Linear Relations Test - 2")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def test003():
    test003counter = 0
    message = ("This test will challenge your skills on functions.")
    title = ("Functions Test - 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = ("There are 10 multiple choice questions. Good luck!")
    title = ("Functions Test - 2")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = (
        "QUESTION 1\n\nWhat function works with the following equation:\nf(x) = |x|"
    )
    title = ("Functions Test - QUESTION 1 / 10")
    output = buttonbox(message, choices=test003Q1)
    if output == test003Q1[3]:
        test003counter += 1
    else:
        test003counter += 0
    message = (
        "QUESTION 2\n\nTrue or False:\nWhen the vertex of a parabola is below the x axis, it opens upwards."
    )
    title = ("Functions Test - QUESTION 2 / 10")
    output = buttonbox(message, choices=test003Q2)
    if output == test003Q2[0]:
        test003counter += 1
    else:
        test003counter += 0
    message = (
        "QUESTION 3\n\nTake into the following equation:\nf(x) = 2x + 5\nWhat will the value of y be when x = 2?"
    )
    title = ("Functions Test - QUESTION 3 / 10")
    output = buttonbox(message, choices=test003Q3)
    if output == test003Q3[1]:
        test003counter += 1
    else:
        test003counter += 0
    message = ("QUESTION 4\n\nWhat does the vertical line test determine?")
    title = ("Functions Test - QUESTION 4 / 10")
    output = buttonbox(message, choices=test003Q4)
    if output == test003Q4[1]:
        test003counter += 1
    else:
        test003counter += 0
    message = (
        "QUESTION 5\n\nWhich of these following functions only has one branch?"
    )
    title = ("Functions Test - QUESTION 5 / 10")
    output = buttonbox(message, choices=test003Q5)
    if output == test003Q5[0]:
        test003counter += 1
    else:
        test003counter += 0
    message = (
        "QUESTION 6\n\nOn the function f(x) = 3x³, what are the y values when x = 1, 2, 3."
    )
    title = ("Functions Test - QUESTION 6 / 10")
    output = buttonbox(message, choices=test003Q6)
    if output == test003Q6[2]:
        test003counter += 1
    else:
        test003counter += 0
    message = (
        "QUESTION 7\n\nWhich of these following functions only has one branch?"
    )
    title = ("Functions Test - QUESTION 7 / 10")
    output = buttonbox(message, choices=test003Q7)
    if output == test003Q7[0]:
        test003counter += 1
    else:
        test003counter += 0
    message = (
        "QUESTION 8\n\nWhich of these following functions only has one branch?"
    )
    title = ("Functions Test - QUESTION 8 / 10")
    output = buttonbox(message, choices=test003Q8)
    if output == test003Q8[3]:
        test003counter += 1
    else:
        test003counter += 0
    message = (
        "QUESTION 9\n\nWhich of these following functions only has one branch?"
    )
    title = ("Functions Test - QUESTION 9 / 10")
    output = buttonbox(message, choices=test003Q9)
    if output == test003Q9[2]:
        test003counter += 1
    else:
        test003counter += 0
    message = (
        "QUESTION 10\n\nWhich of these following functions only has one branch?"
    )
    title = ("Functions Test - QUESTION 10 / 10")
    #This function creates a differing message for each different grade you could have gotten.
    output = buttonbox(message, choices=test003Q10)
    if output == test003Q10[3]:
        test003counter += 1
    else:
        test003counter += 0
    message = ("Your final score was\n\n*initiating drumroll*")
    title = ("Functions Test - Final Results")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    if test003counter == 10:
        message = ("A perfect 10 out of 10. Well done!")
        title = ("Functions Test - Final Results")
        contButton = ("Continue")
        output = msgbox(message, title, contButton)
        menu()
    elif test003counter <= 9 and test003counter >= 7:
        message = (test003counter, "\nNicely done. You almost had it.")
        title = ("Functions Test - Final Results")
        contButton = ("Continue")
        output = msgbox(message, title, contButton)
        menu()
    elif test003counter <= 6 and test003counter >= 5:
        message = (
            test003counter,
            "\nYou did servicably well. A bit more practice and you'll be there."
        )
        title = ("Functions Test - Final Results")
        contButton = ("Continue")
        output = msgbox(message, title, contButton)
        menu()
    elif test003counter <= 4 and test003counter >= 3:
        message = (test003counter, "\nEh... no worries. There's been worse.")
        title = ("Functions Test - Final Results")
        contButton = ("Continue")
        output = msgbox(message, title, contButton)
        menu()
    elif test003counter <= 2 and test003counter >= 1:
        message = (test003counter, "\nYou...got something right.")
        title = ("Functions Test - Final Results")
        contButton = ("Continue")
        output = msgbox(message, title, contButton)
        menu()
    else:
        message = (
            test003counter,
            "\nThere's not much sugarcoating I can do here... you should definitely do some reviewing."
        )
        title = ("Functions Test - Final Results")
        contButton = ("Continue")
        output = msgbox(message, title, contButton)
        menu()


def test004():
    message = ("This test will challenge your skills on polynomials.")
    title = ("Polynomials Test- 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = ("There are 10 multiple choice questions. Good luck!")
    title = ("Polynomials Test- 2")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def test005():
    message = ("This test will challenge your skills on polynomials.")
    title = ("Polynomials Test- 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = ("There are 10 multiple choice questions. Good luck!")
    title = ("Polynomials Test- 2")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def test006():
    message = ("This test will challenge your skills on polynomials.")
    title = ("Polynomials Test- 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = ("There are 10 multiple choice questions. Good luck!")
    title = ("Polynomials Test- 2")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def test007():
    message = ("This test will challenge your skills on polynomials.")
    title = ("Polynomials Test- 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = ("There are 10 multiple choice questions. Good luck!")
    title = ("Polynomials Test- 2")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


def test008():
    message = ("This test will challenge your skills on polynomials.")
    title = ("Polynomials Test- 1")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    message = ("There are 10 multiple choice questions. Good luck!")
    title = ("Polynomials Test- 2")
    contButton = ("Continue")
    output = msgbox(message, title, contButton)
    menu()


#These functions correspond to the buttons on the main menu, leading to user to each different menu. Clicking on the graph picture will lead the user to the graphing section (corresponds to the else).
def GR9T():
    global choices
    global GR9T
    choices = menuOptions[0]
    img = 'GR9T-Screen.png'
    GR9TOutput = buttonbox(image=img, choices=GR9Toptions)
    if GR9TOutput == GR9Toptions[0]:
        lesson001()
    elif GR9TOutput == GR9Toptions[1]:
        lesson002()
    elif GR9TOutput == GR9Toptions[2]:
        menu()


def GR10T():
    global choices
    global GR10T
    choices = menuOptions[1]
    img = 'GR10T-Screen.png'
    GR10TOutput = buttonbox(image=img, choices=GR10Toptions)
    if GR10TOutput == GR10Toptions[0]:
        lesson003()
    elif GR10TOutput == GR10Toptions[1]:
        lesson004()
    elif GR10TOutput == GR10Toptions[2]:
        menu()


def GR11T():
    global choices
    global GR11T
    choices = menuOptions[2]
    img = 'GR11T-Screen.png'
    GR11TOutput = buttonbox(image=img, choices=GR11Toptions)
    if GR11TOutput == GR11Toptions[0]:
        lesson005()
    elif GR11TOutput == GR11Toptions[1]:
        lesson006()
    elif GR11TOutput == GR11Toptions[2]:
        menu()


def GR12T():
    global choices
    global GR12T
    choices = menuOptions[3]
    img = 'GR12T-Screen.png'
    GR12TOutput = buttonbox(image=img, choices=GR12Toptions)
    if GR12TOutput == GR12Toptions[0]:
        lesson007()
    elif GR12TOutput == GR12Toptions[1]:
        lesson008()
    elif GR12TOutput == GR12Toptions[2]:
        menu()


def GR9E():
    global choices
    global GR9E
    choices = menuOptions[4]
    img = 'GR9E-Screen.png'
    GR9EOutput = buttonbox(image=img, choices=GR9Eoptions)
    if GR9EOutput == GR9Eoptions[0]:
        practice001()
    elif GR9EOutput == GR9Eoptions[1]:
        practice002()
    elif GR9EOutput == GR9Eoptions[2]:
        test001()
    elif GR9EOutput == GR9Eoptions[3]:
        test002()
    elif GR9EOutput == GR9Eoptions[4]:
        menu()


def GR10E():
    global choices
    global GR10E
    choices = menuOptions[5]
    img = 'GR10E-Screen.png'
    GR10EOutput = buttonbox(image=img, choices=GR10Eoptions)
    if GR10EOutput == GR10Eoptions[0]:
        practice003()
    elif GR10EOutput == GR10Eoptions[1]:
        practice004()
    elif GR10EOutput == GR10Eoptions[2]:
        test003()
    elif GR10EOutput == GR10Eoptions[3]:
        test004()
    elif GR10EOutput == GR10Eoptions[4]:
        menu()


def GR11E():
    global choices
    global GR11E
    choices = menuOptions[6]
    img = 'GR11E-Screen.png'
    GR11EOutput = buttonbox(image=img, choices=GR11Eoptions)
    if GR11EOutput == GR11Eoptions[0]:
        practice005()
    elif GR11EOutput == GR11Eoptions[1]:
        practice006()
    elif GR11EOutput == GR11Eoptions[2]:
        test005()
    elif GR11EOutput == GR11Eoptions[3]:
        test006()
    elif GR11EOutput == GR11Eoptions[4]:
        menu()


def GR12E():
    global choices
    global GR12E
    choices = menuOptions[7]
    img = 'GR12E-Screen.png'
    GR12EOutput = buttonbox(image=img, choices=GR12Eoptions)
    if GR12EOutput == GR12Eoptions[0]:
        practice005()
    elif GR12EOutput == GR12Eoptions[1]:
        practice006()
    elif GR12EOutput == GR12Eoptions[2]:
        test005()
    elif GR12EOutput == GR12Eoptions[3]:
        test006()
    elif GR12EOutput == GR12Eoptions[4]:
        menu()


#---MENU---

img = logoScreen
output = buttonbox(image=img, choices=activation)


def menu():
    global selection
    img = 'Graph-Button.png'
    selection = buttonbox(image=img, choices=menuOptions)
    if selection == menuOptions[0]:
        GR9T()

    elif selection == menuOptions[1]:
        GR10T()

    elif selection == menuOptions[2]:
        GR11T()

    elif selection == menuOptions[3]:
        GR12T()

    elif selection == menuOptions[4]:
        GR9E()

    elif selection == menuOptions[5]:
        GR10E()

    elif selection == menuOptions[6]:
        GR11E()

    elif selection == menuOptions[7]:
        GR12E()

    else:
        #EVERYTHING ABOVE HAS BEEN CODED BY DYLAN DERGUSON
        #SHOULD BE NOTED THAT WE BOTH AIDED EACHOTHER IN MANY ASPECTS OF OUR RESPECTIVE RESPONSIBILITIES IN THIS PROJECT. WE HAVE EACH COLABORATED ON OUR SECTIONS OF CODE
        #EVERYTHING FROM THIS POINT ON HAS BEEN CODED BY OWEN MCKIBBON
        #Explanation of input
        print(
            "Input equation coefficients. EX: 5x^3 + 2x, would have an input of '5 2 0'. (Spaces between number, brackets with spaces between if multiplying functions, / if dividing):"
        )

        #inputing list as string to be converted to integers
        eq1 = [(s) for s in input().split()]
        eqCs = []
        numer = []
        denom = []
        f = []
        g = []
        x = 0
        y = 0
        #Empty string to be filled with equation
        l = ''
        #creating global variable for first derivative
        global prime

        #QUOTIENT RULE
        #checking for the division in their equation
        if '/' in eq1:
            #Indexing the division within the list
            chopi = eq1.index('/')
            #Creating a loop between the start of the list to the '/'
            for i in range(0, chopi):
                #trying to turn the items within the range to integers to avoid the '/'
                try:
                    eq1[i] = int(eq1[i])
                except:
                    #print("uh oh ")
                    pass
                #Apending everything to the left of '/' to the numerator list
                numer.append(eq1[i])
            #Second loop for the denominator between one more than the index of the '/' to the end
            for i in range(chopi + 1, len(eq1)):
                #turning the coefficients to integers
                try:
                    eq1[i] = int(eq1[i])
                except:
                    pass
                #appending the coefficients to the denominator
                denom.append(eq1[i])

        #PRODUCT RULE
        #if brackets are used for multiplying functions
        elif '(' in eq1 and ')' in eq1:
            #Indexing both brackets to start
            chopC = eq1.index(')')
            chopO = eq1.index('(')
            #Creating a loop from the first open bracket to the first closed
            for i in range(chopO + 1, chopC):
                #converting items between brackets to integers
                try:
                    eq1[i] = int(eq1[i])
                except:
                    pass
                #apending items within the first set of brackets to the first list of f
                f.append(eq1[i])
            #Deleting the items between the first set of brackets, and including the brackets
            del eq1[0:chopC + 1]
            #If they still exist
            if '(' in eq1 and ')' in eq1:
                #Indexing the brackets a second time for the second set of brackets
                chopC = eq1.index(')')
                chopO = eq1.index('(')
                #second loop between second brackets
                for i in range(chopO + 1, chopC):
                    #attempting to convert items to integers
                    try:
                        eq1[i] = int(eq1[i])
                    except:
                        pass
                    #Appending second list to g
                    g.append(eq1[i])
        #If not a product or quotient
        else:
            #Convert to ints
            eqCs = [int(o) for o in eq1]
            #if the length is greater than 1
            if len(eqCs) > 1:
                #for loop for the length of the list - 2 due to loss of item during derivation
                for i in range(len(eqCs) - 2):
                    #new string for the equation to be printed
                    z = ((eqCs[i]) * x**(len(eqCs) - i - 1))
                    y += z
                    l += str(eqCs[i]) + 'x^' + str(len(eqCs) - i - 1) + ' + '
                y += eqCs[-1]
                l += str(eqCs[-2]) + 'x' + ' + '
                l += str(eqCs[-1])
                #printing equation
                print('f(x) =', l)
            else:
                #if it is not greater than 1 it will simply print the only item in the list
                print('f(x) =', eqCs[0])

        #quotient rule for taking the derivative of divided functions

        def quotient():
            #turning the numerator into an equation
            numeq = np.poly1d(numer)
            #turning the denominator into an equation
            boteq = np.poly1d(denom)
            #Taking the derivative of the numerator
            tnum = numeq.deriv()
            #Taking the derivative of the denominator
            tbot = boteq.deriv()
            #Creating equation for numerator over denominator
            equateq = numeq / boteq
            #vairbale for top of derivative equation
            n = (tnum * boteq - tbot * numeq)
            #vairbale for bottom of derivative equation
            d = boteq**2
            #turning the bottom and top of the derivative into equations
            q = np.poly1d(d)
            p = np.poly1d(n)
            #printing them out individually over top of eachother
            print("f(x) = \n", numeq, "\n----------------------------\n",
                  boteq)
            print("\nf'(x) = \n", p, "\n----------------------------\n", q)
            #setting prime as the derivative
            prime = p / q
            prime = np.poly1d
            #returning the original and derivative equation
            return prime, equateq

        #Product rule function
        def product():
            #making equation of first brackets
            feq = np.poly1d(f)
            #making equation of second brackets
            geq = np.poly1d(g)
            #deriving first brackets
            fPrime = feq.deriv()
            #deriving second brackets
            gPrime = geq.deriv()
            #Full equation of derivative
            prime = (fPrime * geq) + (gPrime * feq)
            #Equation of first input
            expanded = feq * geq
            #printing equations
            print("f(x)=\n", expanded)
            print("f'(x)=\n", prime)
            #calculation of x at specific value
            value = int(
                input("Please enter a specific value to calculate f(x): "))
            print(expanded(value))
            #returning equation and derivative
            return prime, expanded

        #Graphing function with peramaters of both original equations
        def polytry(expanded, equateq):
            #https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html
            #Designating x with the endpoints on the x axis of 100
            x = np.linspace(-100, 100, 50, endpoint=True)
            #if there are brackets it graphs the product rule equation
            if '(' in eq1:
                y = expanded
            #If there is a / it graphs the quotient rule equation
            elif '/' in eq1:
                y = equateq
            #otherwise it graphs the regular equation
            else:
                y = feq1
            #the derivative is always prime
            t = prime
            #n = numeq
            ax = pl.gca()  # gca stands for 'get current axis'
            #Creates the spines/ axis of the graph with no change in colours
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            #sets ticks for scale to the bottom on x-axis
            ax.xaxis.set_ticks_position('bottom')
            ax.spines['bottom'].set_position(('data', 0))
            #sets ticks for scale to left on y axis
            ax.yaxis.set_ticks_position('left')
            ax.spines['left'].set_position(('data', 0))

            #https://stackoverflow.com/questions/37352098/plotting-a-polynomial-using-matplotlib-and-coeffiecients
            y = [np.polyval(feq1, i) for i in x]
            t = [np.polyval(prime, i) for i in x]
            plt.plot(x, y)
            #Choice of tangent graph
            chosePlot = int(
                input(
                    "Would you like to see the graph of the tangent? (1 for yes 2 for no): "
                ))
            print("derivative-green, original-blue")
            if chosePlot == 1:
                #plots tangent
                plt.plot(x, t, 'g', label=prime)
            else:
                pass
            #pl.plot(x, C, color="blue",  linewidth=1, linestyle="-")
            #setting the look of the graph
            for label in ax.get_xticklabels() + ax.get_yticklabels():
                label.set_fontsize(16)
                label.set_bbox(
                    dict(facecolor='white', edgecolor='None', alpha=0.65))
            #calling the graphs
            plt.show()

        equateq = []
        expanded = []
        prime = []
        feq1 = []
        #calling each function if used
        if '/' in eq1:
            prime, equateq = quotient()
        elif '(' in eq1 and ')' in eq1:
            prime, expanded = product()
        else:
            if len(eqCs) > 1:
                feq1 = np.poly1d(eqCs)
                prime = feq1.deriv()
                print("f'(x) = \n", prime)
            else:
                print("f'(x) = 0")
        #Optional second derivative
        print("click 1 to take the derivative again: ")
        c2 = int(input())
        if c2 == 1:
            sec = prime.deriv()
            print("f''(x) = \n\n", sec)
        else:
            pass
        #Calling graphing function
        polytry(expanded, equateq)


menu()
