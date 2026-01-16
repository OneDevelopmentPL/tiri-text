#!/usr/bin/env python3
import sys
import webbrowser
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

# Pytania
QA_KEYWORDS = {
    "hello": "Hello! How are you?",
    "hi": "Hi there! How can I help?",
    "hey": "Hey! What's up?",
    "how are you": "I'm fine, thank you!",
    "what's up": "Not much! Ready to help you!",
    "bye": "Goodbye! See you later!",
    "goodbye": "Take care! Have a great day!",
    "thanks": "You're welcome! Happy to help!",
    "thank you": "My pleasure! Anytime!",
    "help": "I'm here to answer your questions. Try asking me something!",
    "what can you do": "I can answer simple questions. Try saying hello or asking how I am!",
    "who are you": "I'm your friendly desktop assistant!",
    "your name": "I'm Neon Siri, your AI companion!",
    "time": "I don't have access to the clock, but you can check your system tray!",
    "weather": "I can't check the weather yet, but it's always sunny when we chat! ☀️",
    "joke": "Why did the programmer quit? Because they didn't get arrays! 😄",
    "tell me a joke": "What's a computer's favorite snack? Microchips! 🍟",
    "how old are you": "I'm timeless! Just like good code! ⏰",
    "where are you from": "I'm from the digital realm, here to assist you!",
    "good morning": "Good morning! Hope you have a wonderful day! 🌅",
    "good night": "Good night! Sweet dreams! 🌙",
    "good afternoon": "Good afternoon! Hope your day is going well!",
    "what is your purpose": "My purpose is to make your day a little brighter and answer your questions!",
    "are you real": "I'm as real as code can be! 💻",
    "do you like me": "Of course! You're my favorite user! ❤️",
    "love you": "Aww, that's sweet! I appreciate you too! 💙",
    "sorry": "No worries at all! We're all good!",
    "help me": "Sure! What do you need help with?",
    "awesome": "You're awesome too! 🌟",
    "cool": "Thanks! You're pretty cool yourself! 😎",
    "yes": "Great! Anything else I can help with?",
    "no": "Alright! Let me know if you need anything!",
}

def get_answer(query: str) -> str:
    q = query.lower()
    if q.startswith("search ") or q.startswith("google "):
        search_query = query[7:]
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            return f"🔍 Searching for: {search_query}"
        return "Please specify what to search for!"
    for keyword, answer in QA_KEYWORDS.items():
        if keyword in q:
            return answer
    return f"I don't know that. Type 'search {query}' to look it up! 🔍"

class NeonSiri(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.setFixedSize(400, 300)

        self.setStyleSheet("""
            QWidget {
                background-color: rgba(0, 0, 0, 180);
                border-radius: 20px;
            }
            QLabel {
                color: white;
            }
            QPushButton {
                color: white;
                background: rgba(255, 0, 0, 180);
                border: none;
                border-radius: 10px;
                padding: 6px;
            }
            QPushButton:hover {
                background: rgba(255, 0, 0, 230);
            }
        """)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Ikona
        self.icon_label = QLabel()
        pix = QPixmap("/home/iwo/Pobrane/obraz-removebg-preview.png")
        pix = pix.scaled(64, 64, Qt.AspectRatioMode.KeepAspectRatio,
                         Qt.TransformationMode.SmoothTransformation)
        self.icon_label.setPixmap(pix)
        self.icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.icon_label)

        # Pole tekstowe
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your question or 'search ...'")
        self.layout.addWidget(self.input_field)

        # Odpowiedź
        self.response_label = QLabel("")
        self.response_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.response_label)

        # Przycisk zamknięcia
        self.close_button = QPushButton("✖")
        self.close_button.clicked.connect(self.close)
        self.layout.addWidget(self.close_button)

        self.input_field.returnPressed.connect(self.on_enter)

    def showInTopRight(self):
        screen_geom = QApplication.primaryScreen().availableGeometry()
        x = screen_geom.x() + screen_geom.width() - self.width() - 20
        y = screen_geom.y() + 20
        self.move(x, y)
        self.show()

    def on_enter(self):
        text = self.input_field.text().strip()
        if not text:
            return
        ans = get_answer(text)
        self.response_label.setText(ans)
        self.input_field.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NeonSiri()
    window.showInTopRight()
    sys.exit(app.exec())
