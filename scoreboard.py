from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("high_score.txt", 'r') as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        if self.high_score > 0:
            self.write(f'Score: {self.score} High Score: {self.high_score}', False, align=ALIGNMENT, font=FONT)
        else:
            self.write(f'Score: {self.score}', False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
