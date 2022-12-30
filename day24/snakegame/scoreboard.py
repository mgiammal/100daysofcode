from turtle import Turtle

OFFSET = 30


class ScoreBoard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.sety(screen_height/2 - OFFSET)
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.speed("fastest")
        self.hideturtle()
        self.pencolor("white")
        self.font = ("Courier", 20, "normal")
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.high_score}", align="center", font=self.font)

    def increase_score(self):
        self.score += 1
        self.update_board()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_board()
