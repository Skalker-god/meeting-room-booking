from domain.booking import Booking

class BookRoomUseCase:

    def __init__(self, booking_repository):
        self.booking_repository = booking_repository

    def execute(self, room_id, start_time, end_time):

        new_booking = Booking(room_id, start_time, end_time)

        existing_bookings = self.booking_repository.get_bookings_for_room(room_id)

        for booking in existing_bookings:
            if new_booking.overlaps(booking):
                raise Exception("Time slot already booked")

        self.booking_repository.save(new_booking)

        return new_booking