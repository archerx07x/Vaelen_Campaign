class World:
    """Represents the game world."""

    def __init__(self):
        self.day = 1
        self.year = 1000
        self.season = "Spring"

    def advance_day(self):
        self.day += 1

        if self.day > 90:
            self.day = 1
            self.advance_season()

    def advance_season(self):
        seasons = ["Spring", "Summer", "Autumn", "Winter"]

        current = seasons.index(self.season)

        if current == 3:
            self.season = "Spring"
            self.year += 1
        else:
            self.season = seasons[current + 1]