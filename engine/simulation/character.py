class Character:
    """Represents a person in the world."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.alive = True

    def advance_day(self):
        """Update the character each day."""
        pass