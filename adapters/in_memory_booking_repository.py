class InMemoryBookingRepository:

    def __init__(self):
        self.bookings = []

    def get_bookings_for_room(self, room_id):
        return [b for b in self.bookings if b.room_id == room_id]

    def save(self, booking):
        self.bookings.append(booking)