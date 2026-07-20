from engine.simulation.world import World


class VaelenEngine:
    """The central game engine."""

    def __init__(self):
        self.running = False
        self.world = World()

    def display_header(self):
        print("\n" + "=" * 40)
        print(f"YEAR {self.world.year} | {self.world.season} | DAY {self.world.day}")
        print("=" * 40)

    def start(self):
        self.running = True

        while self.running:
            self.display_header()

            command = input("> ").strip().lower()

            if command == "help":
                print("Commands:")
                print("  help  - Show commands")
                print("  next  - Advance one day")
                print("  character - Display the player character sheet")
                print("  xp <amount> - Give the player experience")
                print("  spend <stat> - Spend one point on a character stat")
                print("  quit  - Exit game")

            elif command == "next":
                self.world.advance_day()
                print("A day passes...")
            elif command == "character":
                player = self.world.characters[0]
                print(player.display_sheet())
            
            elif command.startswith("xp "):
                player = self.world.characters[0]

                try:
                    amount = int(command.split()[1])
                    player.gain_experience(amount)
                    print(f"\nGained {amount} experience.")
                    print(player.display_sheet())
                except (ValueError, IndexError):
                    print("Usage: xp <amount>")
            
            elif command.startswith("spend "):
                player = self.world.characters[0]
                stat_name = command.split()[1].lower()

                if player.spend_stat_point(stat_name):
                    print(f"\nIncreased {stat_name} by 1.")
                    print(player.display_sheet())
                else:
                    print(
                        "\nUnable to spent stat point. "
                        "Check the stat name and your available points."
                    )
            
            elif command == "test":
                player = self.world.characters[0]

                player.current_health = 50
                player.current_stamina = 40

                print("\nBefore:\n")
                print(player.display_sheet())

                player.modify_stat("endurance", 2)

                print("\nAfter gaining +2 Endurance:\n")
                print(player.display_sheet())

            elif command == "quit":
                self.running = False

            else:
                print("Unknown command.")

        print("Game closed.")