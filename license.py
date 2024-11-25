from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import sys
import subprocess
from datetime import datetime, timedelta  # Ensure timedelta is imported

# Set today's date (hardcoded) and the expiration date (6 months later)
TODAY_DATE = datetime(2024, 11, 24)  # Replace with the current date
EXPIRATION_DATE = TODAY_DATE + timedelta(days=6 * 30)  # Approximation for 6 months

def validate_license():
    entered_key = entry.text()
    current_date = TODAY_DATE  # Use hardcoded today date

    # Check if the license is valid and not expired
    if entered_key == "code":
        if current_date <= EXPIRATION_DATE:
            QMessageBox.information(window, "Success", "License valid! Opening the application...")
            open_app()
        else:
            QMessageBox.critical(window, "Error", "License expired. Please contact support.")
    else:
        QMessageBox.critical(window, "Error", "Invalid license key. Please try again.")

def open_app():
    app_path = "/Users/hamedhasibi/Downloads/Vision/Vision Client Launcher/visionclientlauncher.exe"
    subprocess.Popen(["open", app_path])

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("License Validator")
window.setStyleSheet("""
    QWidget {
        background-image: url('bckgrd.webp');
        background-repeat: no-repeat;
        background-position: center;
    }
""")
layout = QVBoxLayout()

label = QLabel("Enter License Key:")
layout.addWidget(label)

entry = QLineEdit()
entry.setEchoMode(QLineEdit.Password)  # Mask input
layout.addWidget(entry)

button = QPushButton("Validate")
button.clicked.connect(validate_license)
layout.addWidget(button)

window.setLayout(layout)
window.resize(800, 600)
window.show()

sys.exit(app.exec_())