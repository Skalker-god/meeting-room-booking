class ConsoleController:

    def __init__(self, use_case):
        self.use_case = use_case

    def run(self):

        while True:
            print("\n--- Room Booking ---")

            room = input("Room ID: ")
            start = int(input("Start time: "))
            end = int(input("End time: "))

            try:
                booking = self.use_case.execute(room, start, end)
                print("Booking created!")

            except Exception as e:
                print("Error:", e)

            again = input("Create another booking? (y/n): ")

            if again.lower() != "y":
                break
