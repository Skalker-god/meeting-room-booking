from abc import ABC, abstractmethod

class BookingRepository(ABC):

    @abstractmethod
    def get_bookings_for_room(self, room_id):
        pass

    @abstractmethod
    def save(self, booking):
        pass