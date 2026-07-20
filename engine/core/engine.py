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
                print("  quit  - Exit game")

            elif command == "next":
                self.world.advance_day()
                print("A day passes...")
            elif command == "character":
                player = self.world.characters[0]
                print(player.display_sheet())
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