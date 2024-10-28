import sys
import base64
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QMessageBox
)

class Base64App(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set up the UI
        self.setWindowTitle('Base64 Encoder/Decoder')
        self.setGeometry(300, 300, 400, 350)
        
        layout = QVBoxLayout()

        # Input field
        self.input_label = QLabel('Input:')
        layout.addWidget(self.input_label)
        self.input_text = QTextEdit()
        layout.addWidget(self.input_text)

        # Encode Button
        self.encode_button = QPushButton('Encode to Base64')
        self.encode_button.clicked.connect(self.encode_base64)
        layout.addWidget(self.encode_button)

        # Decode Button
        self.decode_button = QPushButton('Decode from Base64')
        self.decode_button.clicked.connect(self.decode_base64)
        layout.addWidget(self.decode_button)

        # Output field
        self.output_label = QLabel('Output:')
        layout.addWidget(self.output_label)
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        # Copy Button
        self.copy_button = QPushButton('Copy Output')
        self.copy_button.clicked.connect(self.copy_output)
        layout.addWidget(self.copy_button)
        
        # Set the layout
        self.setLayout(layout)

    def encode_base64(self):
        # Get the text from the input field
        input_data = self.input_text.toPlainText()
        if not input_data:
            QMessageBox.warning(self, "Input Error", "Please provide some input to encode.")
            return
        
        # Encode the input to Base64
        encoded_data = base64.b64encode(input_data.encode('utf-8')).decode('utf-8')
        
        # Display the encoded data in the output field
        self.output_text.setText(encoded_data)

    def decode_base64(self):
        # Get the text from the input field
        input_data = self.input_text.toPlainText()
        if not input_data:
            QMessageBox.warning(self, "Input Error", "Please provide some input to decode.")
            return

        try:
            # Decode the input from Base64
            decoded_data = base64.b64decode(input_data).decode('utf-8')
        except Exception as e:
            QMessageBox.warning(self, "Decoding Error", f"Failed to decode: {e}")
            return
        
        # Display the decoded data in the output field
        self.output_text.setText(decoded_data)

    def copy_output(self):
        # Copy the output text to the clipboard
        output_data = self.output_text.toPlainText()
        if output_data:
            clipboard = QApplication.clipboard()
            clipboard.setText(output_data)
            QMessageBox.information(self, "Copied", "Output copied to clipboard!")
        else:
            QMessageBox.warning(self, "No Output", "There is no output to copy.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Base64App()
    window.show()
    sys.exit(app.exec_())
