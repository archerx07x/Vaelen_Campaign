class VaelenEngine:
    """The central game engine."""

    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        print("=== VAELEN ENGINE STARTED ===")

        while self.running:
            command = input("> ").strip().lower()

            if command == "quit":
                self.running = False
            elif command == "help":
                print("Commands: help, quit")
            else:
                print(f"Unknown command: {command}")

        print("=== VAELEN ENGINE STOPPED ===")