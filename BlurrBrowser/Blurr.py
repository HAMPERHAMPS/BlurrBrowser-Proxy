#from PyQt5.QtCore import QUrl
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtWidgets import QApplication
#import sys

#app = QApplication(sys.argv)
#browser = QWebEngineView()
#browser.setUrl(QUrl("HampGX_Frame.html"))
#browser.setWindowTitle("Blurr")

#browser.show()
#sys.exit(app.exec_())
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

class BrowserWindow(QMainWindow):
    def __init__(self, url):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))
        self.setCentralWidget(self.browser)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Blurr")
        self.show()

        # Handle window closing
        self.browser.page().profile().downloadRequested.connect(self.on_closing)

    def on_closing(self, download):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Blurr")
    url = "https://www.bing.com"
    
    # Additional setup for Windows to prevent subprocess errors
    sys_argv = sys.argv
    sys_argv.append("--no-sandbox")

    window = BrowserWindow(url)
    sys.exit(app.exec_())

