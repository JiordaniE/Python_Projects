#imports the module turtle
import turtle

#goes into the turtle module to get the "class" Turtle
#the "()" is used to make an object from the blueprint
#saved all of it as "timmy
#uppercase T in Turtle means it's a class
timmy = turtle.Turtle()

print(timmy)

#another way to import turtle module and Turtle class

from turtle import Turtle, Screen

print(timmy)
#makes timmy into a turtle shape
timmy.shape("turtle")
#changes the color of the turtle, and requires an actual string of color
timmy.color("coral")
#make timmy move 100 paces
timmy.forward(100)

#screen is the attribute
my_screen = Screen()
print(my_screen.canvheight)
#makes you exit the image with a click
my_screen.exitonclick()

#importing prettytable
from prettytable import PrettyTable
table = PrettyTable()

#makes table columns
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

#makes the second column
table.add_column("Type", ["Electric", "Water", "Fire"])

#make inputs left aligned using attributes.
table.align = "l"

print(table)
