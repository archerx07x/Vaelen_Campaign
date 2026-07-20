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
                print("  quit  - Exit game")

            elif command == "next":
                self.world.advance_day()
                print("A day passes...")

            elif command == "quit":
                self.running = False

            else:
                print("Unknown command.")

        print("Game closed.")