from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]

class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.snake.append(new_segment)

    def reset(self):
        for segment in self.snake:
            segment.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def extend(self):
        #adds new segment to snake
        self.add_segment(self.snake[-1].position())

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            self.new_x = self.snake[seg_num - 1].xcor()
            self.new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(self.new_x, self.new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
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

