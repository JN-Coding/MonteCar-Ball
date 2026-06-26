class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players

    def total_plus_minus(self):
        return sum(p.avg_plus_minus for p in self.players)
    
    def total_pts(self):
        return sum(p.avg_pts for p in self.players)
    