import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setGeometry(550, 550, 500, 300)
window.setWindowTitle("Library Kevin")
window.show()

sys.exit(app.exec())