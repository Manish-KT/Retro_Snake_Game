from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        for i in range(3):
            torti = Turtle(shape="square")
            torti.penup()
            torti.color("white")
            torti.goto(x, 0)
            x -= 20
            self.segments.append(torti)

    def extend(self):
        torti = Turtle(shape="square")
        torti.penup()
        torti.color("white")
        torti.goto(self.segments[-1].position())
        self.segments.append(torti)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == 180:
            self.head.right(90)

        if self.head.heading() == 0:
            self.head.left(90)

    def down(self):
        if self.head.heading() == 180:
            self.head.right(-90)

        if self.head.heading() == 0:
            self.head.left(-90)

        # or we can use setheading method and put direction in it.
    def left(self):
        if self.head.heading() == 90:
            self.head.left(90)

        if self.head.heading() == 270:
            self.head.right(90)

    def right(self):
        if self.head.heading() == 90:
            self.head.right(90)

        if self.head.heading() == 270:
            self.head.left(90)
