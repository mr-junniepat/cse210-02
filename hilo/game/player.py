class Player:

    def __init__(self):
        self.hi_low_guess = ""
        self.scoretaken = 300
    
    def update_score(self, scoretaken):
        self.scoretaken += scoretaken