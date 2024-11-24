from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import sys
import subprocess

def validate_license():
    entered_key = entry.text()
    if entered_key == "code":
        QMessageBox.information(window, "Success", "License valid! Opening the application...")
        open_app()
    else:
        QMessageBox.critical(window, "Error", "Invalid license key. Please try again.")

def open_app():
    app_path = "/path/to/your/app_or_exe"
    subprocess.Popen(["open", app_path])

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("License Validator")
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
window.resize(200, 100)
window.show()

sys.exit(app.exec_())