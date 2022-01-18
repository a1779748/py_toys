from turtle import Turtle

# constant the starting position of our snake
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
# constant move distance
MOVE_DISTANCE = 20
# constant direction
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # current snake
        self.segments = []
        # call create snake method
        self.create_snake()
        # the head of our snake
        self.head = self.segments[0]

    def create_snake(self):
        """
        create a circle shaped white snake
        :return:
        """
        # filling the snake on the screen
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """
        draw/add a new segment to current snake's body
        :param position:
        :return:
        """
        new_segment = Turtle(shape="circle")
        new_segment.color("white")
        # pull the pen up, not drawing when move
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        move snake: each time we move 2nd to 1st, move 3rd to 2nd, so on and so forth...
        :return:
        """
        # for seg_num in range(start=2, stop=0, step=-1)
        # move snake one segment per step
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

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

