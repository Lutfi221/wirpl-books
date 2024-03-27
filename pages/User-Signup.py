import time

from wirpl_books.services.user import UserService


user_service = UserService()
# Pakai `int(time.time())` untuk membuat ID unik
# user_service.register(int(time.time()), "John Doe", "123 Main St", "john.doe@example", "M")
