from turtle import Turtle

FONT = ("Courier", 24, "normal")
OFFSET = 40


class Scoreboard(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.pu()
        self.sety(screen_height/2 - OFFSET)
        self.setx(-screen_width/2 + 20)
        self.level = 0
        self.speed("fastest")
        self.hideturtle()
        self.pencolor("black")
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
