from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

# with open('data.txt', mode='w') as high_score_file:


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as high_score_file:
            self.high_score = int(high_score_file.read())
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.color('white')
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as high_score_file:
                high_score_file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
