"""TODO: Creating a turtle inspired by Piet Mondrian usin Atmospheric Perspective."""

__author__ = "730718451"

from turtle import Turtle, colormode, done


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
    # Sequence below makes use of the square function to create the rest of the turtle objects.
    square(piet, 175, 175, 45, "light steel blue", "light steel blue")
    square(piet, 125, 125, 60, "cornflower blue", "cornflower blue")
    square(piet, 75, 75, 90, "royal blue", "royal blue")
    square(piet, 25, 25, 120, "blue", "blue")
    square(piet, -90, -90, 180, "medium blue", "medium blue")
    square(piet, -210, -210, 260, "navy", "navy")
    square(piet, -290, -290, 300, "midnight blue", "midnight blue")
    done()


def square(piet: Turtle, x: float, y: float, length: float, color: str, pencolor: str) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    # Does the job of repreating the procedure for the main function.
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


if __name__ == "__main__": main()
# Calls back the main function.