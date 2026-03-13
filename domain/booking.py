class Booking:
    def __init__(self, room_id, start_time, end_time):
        self.room_id = room_id
        self.start_time = start_time
        self.end_time = end_time

    def overlaps(self, other):
        return (
                self.room_id == other.room_id and
                self.start_time < other.end_time and
                self.end_time > other.start_time
        )