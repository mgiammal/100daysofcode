from turtle import Turtle

OFFSET = 30


class ScoreBoard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.sety(screen_height/2 - OFFSET)
        self.left_score = 0
        self.right_score = 0
        self.speed("fastest")
        self.hideturtle()
        self.pencolor("white")
        self.font = ("Courier", 20, "normal")
        self.update_board()

    def update_board(self):
        self.write(f"{self.left_score}   {self.right_score}", align="center", font=self.font)

    def increase_score_l(self):
        self.clear()
        self.left_score += 1
        self.update_board()

    def increase_score_r(self):
        self.clear()
        self.right_score += 1
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=self.font)
