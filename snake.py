from turtle import Screen, Turtle
import time

#Declare constant, easier to change
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake():
    def __init__(self):
        self.all_squares = []
        self.create_snake()
        self.head = self.all_squares[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def add_square(self, position):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.goto(position)
        self.all_squares.append(new_part)

    def reset(self):
        for i in self.all_squares:
            i.goto(1000, 1000)
        self.all_squares.clear()
        # Initialise the snake again
        self.create_snake()
        self.head = self.all_squares[0]

    def extend(self):
        # Add a new square to the same position as the last square of the snake
        self.add_square(self.all_squares[-1].position())

    def move(self):
        ## Make the snake to auto moves forward, allow the tail to allow the direction of the head
        # for i in range(start= 2, stop= 0, range= -1):
        for i in range(len(self.all_squares) - 1, 0, -1):
            new_x = self.all_squares[i - 1].xcor()
            new_y = self.all_squares[i - 1].ycor()
            self.all_squares[i].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        #not self.head only, if not the body wont be following. self.head is an individual head.
        #in order for the body to follow the direction of the head, use self.head.heading()
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)