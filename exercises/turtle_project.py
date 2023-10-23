"""TODO: Creating a turtle inspired by Piet Mondrian using Atmospheric Perspective."""

__author__ = "730718451"

from turtle import Turtle, done


def main() -> None:
    """The entrypoint of my scene."""
    # Constructs the first Turtle object.
    piet: Turtle = Turtle()
    piet.penup()
    piet.goto(200, 200)
    piet.pendown()
    piet.pencolor("light blue")
    i: int = 0
    piet.begin_fill()
    while (i < 4):
        piet.fillcolor("light blue")
        piet.forward(30)
        piet.left(90)
        i = i + 1
    piet.end_fill()
    # Sequence below makes use of each function to create the rest of the turtle objects.
    square(piet, 175, 175, 45, "light steel blue", "light steel blue")
    square(piet, 125, 125, 60, "cornflower blue", "cornflower blue")
    square(piet, 75, 75, 90, "royal blue", "royal blue")
    square(piet, 25, 25, 120, "blue", "blue")
    square(piet, -90, -90, 180, "medium blue", "medium blue")
    square(piet, -210, -210, 260, "navy", "navy")
    square(piet, -290, -290, 300, "midnight blue", "midnight blue")
    triangle(piet, 275, 275, 45, 120, "pale green", "pale green")
    triangle(piet, 260, 230, 60, 120, "light green", "light green")
    triangle(piet, 245, 170, 90, 120, "spring green", "spring green")
    triangle(piet, 220, 100, 120, 120, "lime green", "lime green")
    triangle(piet, 180, 25, 180, 120, "green", "green")
    triangle(piet, 145, -90, 260, 120, "forest green", "forest green")
    triangle(piet, 100, -175, 300, 120, "dark green", "dark green")
    rectangle(piet, 70, 200, 45, 10, "peach puff", "peach puff")
    rectangle(piet, 35, 200, 25, 60, "light salmon", "light salmon")
    rectangle(piet, 30, 180, 110, 50, "coral", "coral")
    rectangle(piet, -10, 80, 80, 160, "tomato", "tomato")
    rectangle(piet, -270, 15, 210, 120, "red", "red")
    rectangle(piet, -380, 60, 190, 265, "crimson", "crimson")
    line(piet, 190, 190, 45)
    line(piet, 160, 160, 60)
    line(piet, 100, 100, 90)
    line(piet, 55, 55, 120)
    line(piet, -55, -55, 180)
    line(piet, -190, -190, 260)
    line(piet, -245, -245, 300)
    done()


def square(piet: Turtle, x: float, y: float, length: float, color: str, pencolor: str) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    # Does the job of repreating the square procedure for the main function.
    piet.penup()
    piet.goto(x, y)
    piet.pendown()
    piet.pencolor(pencolor)
    i: int = 0
    piet.begin_fill()
    while (i < 4):
        piet.fillcolor(color)
        piet.forward(length)
        piet.left(90)
        i = i + 1
    piet.end_fill()


def triangle(piet: Turtle, x: float, y: float, length: float, angle: float, color: str, pencolor: str) -> None:
    """Draw a triangle of the given width whose top-left corner is located at x, y."""
    # Does the job of repreating the triangle procedure for the main function.
    piet.penup()
    piet.goto(x, y)
    piet.pendown()
    piet.pencolor(pencolor)
    i: int = 0
    piet.begin_fill()
    while (i < 3):
        piet.fillcolor(color)
        piet.forward(length)
        piet.left(angle)
        i = i + 1
    piet.end_fill()


def rectangle(piet: Turtle, x: float, y: float, length: float, width: float, color: str, pencolor: str) -> None:
    """Draw a rectangle of the given width whose top-left corner is located at x, y."""
    # Does the job of repreating the rectangle procedure for the main function.
    piet.penup()
    piet.goto(x, y)
    piet.pendown()
    piet.pencolor(pencolor)
    piet.begin_fill()
    piet.fillcolor(color)
    piet.forward(length)
    piet.left(90)
    piet.forward(width)
    piet.left(90)
    piet.forward(length)
    piet.left(90)
    piet.forward(width)
    piet.end_fill()


def line(piet: Turtle, x: float, y: float, length: float) -> None:
    """Draw a line of the given length that starts at x, y."""
    # Does the job of repreating the line procedure for the main function.
    piet.penup()
    piet.goto(x, y)
    piet.pendown()
    piet.pencolor("black")
    piet.forward(length)


if __name__ == "__main__": 
    main()
# Calls back the main function.