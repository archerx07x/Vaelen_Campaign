class Character:
    """Represents a person in the world."""

    def __init__(
        self,
        name,
        age,
        strength=10,
        agility=10,
        endurance=10,
        intelligence=10,
        charisma=10,
    ):
        self.name = name
        self.age = age
        self.alive = True

        self.base_strength = strength
        self.base_agility = agility
        self.base_endurance = endurance
        self.base_intelligence = intelligence
        self.base_charisma = charisma

        self.current_health = self.max_health
        self.current_stamina = self.max_stamina

        self.level = 1
        self.experience = 0
        self.experience_to_next_level = 100

        self.unspent_stat_points = 0

    @property
    def max_health(self):
        """Calculate maximum health from endurance."""
        return self.base_endurance * 10

    @property
    def max_stamina(self):
        """Calculate maximum stamina from endurance and agility."""
        return (self.base_endurance * 5) + (self.base_agility * 5)

    @property
    def carry_weight(self):
        """Calculate carrying capacity from strength."""
        return self.base_strength * 5

    def modify_stat(self, stat_name, amount):
        """Change a base stat while preserving related resource percentages."""

        stat_attributes = {
           "strength": "base_strength",
           "agility": "base_agility",
           "endurance": "base_endurance",
           "intelligence": "base_intelligence",
           "charisma": "base_charisma",
    }

        if stat_name not in stat_attributes:
         raise ValueError(f"Unknown stat: {stat_name}")

        old_max_health = self.max_health
        old_max_stamina = self.max_stamina

        health_ratio = self.current_health / old_max_health
        stamina_ratio = self.current_stamina / old_max_stamina

        attribute_name = stat_attributes[stat_name]

        current_value = getattr(self, attribute_name)
        new_value = max(1, current_value + amount)

        setattr(self, attribute_name, new_value)

        self.current_health = round(self.max_health * health_ratio)
        self.current_stamina = round(self.max_stamina * stamina_ratio)

        self.current_health = min(self.current_health, self.max_health)
        self.current_stamina = min(self.current_stamina, self.max_stamina)
    
    def display_sheet(self):
        """Return a formatted character sheet."""
        return (
            f"\n"
            f"=========================\n"
            f"{self.name}\n"
            f"Age: {self.age}\n\n"
            f"Level:        {self.level}\n"
            f"Experience:   {self.experience}/{self.experience_to_next_level}\n"
            f"Stat Points:  {self.unspent_stat_points}\n\n"
            f"Strength:     {self.base_strength}\n"
            f"Agility:      {self.base_agility}\n"
            f"Endurance:    {self.base_endurance}\n"
            f"Intelligence: {self.base_intelligence}\n"
            f"Charisma:     {self.base_charisma}\n\n"
            f"Health:       {self.current_health}/{self.max_health}\n"
            f"Stamina:      {self.current_stamina}/{self.max_stamina}\n"
            f"Carry Weight: {self.carry_weight}\n"
            f"========================="
        )

    def advance_day(self):
        """Update the character each day."""
        pass