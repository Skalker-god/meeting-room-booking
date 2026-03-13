from application.book_room_use_case import BookRoomUseCase
from adapters.in_memory_booking_repository import InMemoryBookingRepository
from interface.console_controller import ConsoleController

repository = InMemoryBookingRepository()

use_case = BookRoomUseCase(repository)

controller = ConsoleController(use_case)

controller.run()