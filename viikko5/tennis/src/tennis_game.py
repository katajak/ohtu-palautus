class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score = self.p1_score + 1
        else:
            self.p2_score = self.p2_score + 1

    def get_score(self):
        self.score_text = ""

        if self.check_tie():
            return self.score_text

        elif self.check_game_point():
            return self.score_text

        else:
            self.score_to_text(self.p1_score)
            self.score_text = self.score_text + "-"
            self.score_to_text(self.p2_score)
            return self.score_text
    
    def check_tie(self):
        if self.p1_score == self.p2_score:
            if self.p1_score == 0:
                self.score_text = "Love-All"
            elif self.p1_score == 1:
                self.score_text = "Fifteen-All"
            elif self.p1_score == 2:
                self.score_text = "Thirty-All"
            elif self.p1_score == 3:
                self.score_text = "Forty-All"
            else:
                self.score_text = "Deuce"
            return True

    def check_game_point(self):
        if self.p1_score >= 4 or self.p2_score >= 4:
            score_difference = self.p1_score - self. p2_score
            if score_difference == 1:
                self.score_text = "Advantage player1"
            elif score_difference == -1:
                self.score_text = "Advantage player2"
            elif score_difference >= 2:
                self.score_text = "Win for player1"
            else:
                self.score_text = "Win for player2"
            return True

    def score_to_text(self, score):
        if score == 0:
            self.score_text = self.score_text + "Love"
        elif score == 1:
            self.score_text = self.score_text + "Fifteen"
        elif score == 2:
            self.score_text = self.score_text + "Thirty"
        elif score == 3:
            self.score_text = self.score_text + "Forty"
