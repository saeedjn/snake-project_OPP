import json
from color import WHITE

class ScoreManager:
    def __init__(self, file_path="score.json"):
        self.score = 0
        self.high_score = 0
        self.path_file = file_path
        self.load_high_score()

    def add_score(self,points=1):
        self.score += points
        if self.score > self.high_score:
            self.high_score = self.score

    def reset_score(self):
        self.score = 0

    def load_high_score(self):
        try:
            with open(self.path_file, "r") as f:
                data = json.load(f)
                self.high_score = data.get("high_score",0)
        except (FileNotFoundError, json.JSONDecodeError):
            self.high_score = 0

    def save_high_score(self):
        with open(self.path_file, "w") as f:
            json.dump({"high_score" : self.high_score}, f)

    def draw(self,surface,font,x=10, y=10):
        score_text = font.render(f"Score: {self.score}", True,WHITE)
        high_score_text = font.render(f"High Score: {self.high_score}", True,WHITE)
        surface.blit(score_text,(x,y))
        surface.blit(high_score_text,(x,y + 30))


