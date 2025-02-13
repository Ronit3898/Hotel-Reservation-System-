from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QMovie
from qt_material import apply_stylesheet
import sys

class HotelApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setGeometry(300, 200, 800, 500)
        self.setWindowTitle("Hotel Reservation System")

        # Set animated background
        self.bg_label = QLabel(self)
        self.bg_label.setGeometry(0, 0, 800, 500)

        self.movie = QMovie("animated_bg.gif")  # Replace with your animated GIF
        self.bg_label.setMovie(self.movie)
        self.movie.start()

        # Guest ID Label & Input
        self.guest_label = QLabel("Guest ID:", self)
        self.guest_label.move(50, 100)
        self.guest_id = QLineEdit(self)
        self.guest_id.setGeometry(150, 100, 200, 30)

        # Room ID Label & Input
        self.room_label = QLabel("Room ID:", self)
        self.room_label.move(50, 150)
        self.room_id = QLineEdit(self)
        self.room_id.setGeometry(150, 150, 200, 30)

        # Book Room Button
        self.book_button = QPushButton("Book Room", self)
        self.book_button.setGeometry(150, 200, 100, 40)
        self.book_button.clicked.connect(self.book_room)

        # Status Label
        self.status_label = QLabel("", self)
        self.status_label.setGeometry(150, 250, 300, 30)

    def book_room(self):
        guest_id = self.guest_id.text().strip()
        room_id = self.room_id.text().strip()

        if not guest_id or not room_id:
            self.status_label.setText("Please enter both Guest ID and Room ID!")
            return
        
        # Simulate successful booking (Replace this with actual database logic)
        self.status_label.setText(f"Room {room_id} booked for Guest {guest_id}!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_teal.xml")  # Apply material theme

    window = HotelApp()
    window.show()
    
    sys.exit(app.exec_())  # Start the event loop
