import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QGridLayout, QLabel, QScrollArea
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QPixmap, QDesktopServices

class FolderGrid(QWidget):
    def __init__(self, folder_path):
        super().__init__()
        self.layout = QGridLayout(self)
        self.populate_grid(folder_path)

    def populate_grid(self, folder_path):
        folder_paths = [os.path.join(folder_path, folder) for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]
        for i, folder_path in enumerate(folder_paths):
            folder_label = QLabel(self)
            folder_label.setPixmap(QPixmap("folder_icon.png").scaled(100, 100, Qt.KeepAspectRatio))
            folder_label.setAlignment(Qt.AlignCenter)
            folder_label.setText(os.path.basename(folder_path))
            folder_label.setStyleSheet("font-size: 14px;")
            folder_label.setFixedSize(120, 140)
            folder_label.setProperty("folder_path", folder_path)
            folder_label.mouseDoubleClickEvent = lambda event, folder_path=folder_path: self.open_folder(folder_path)
            row = i // 3
            col = i % 3
            self.layout.addWidget(folder_label, row, col)

    def open_folder(self, folder_path):
        QDesktopServices.openUrl(QUrl.fromLocalFile(folder_path))


class MainWindow(QWidget):
    def __init__(self, folder_path):
        super().__init__()
        self.setWindowTitle("Folder Viewer")
        self.setGeometry(100, 100, 400, 400)
        
        # Create QTabWidget
        self.tab_widget = QTabWidget(self)
        
        # Create scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        # Add folder grid to the scroll area
        folder_grid = FolderGrid(folder_path)
        scroll_area.setWidget(folder_grid)
        
        # Add scroll area to the tab
        self.tab_widget.addTab(scroll_area, "Folders")
        
        # Main layout
        main_layout = QGridLayout(self)
        main_layout.addWidget(self.tab_widget)
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Directory to display folders from
    folder_path = "C:/Users/Vex/"
    
    window = MainWindow(folder_path)
    window.show()
    
    sys.exit(app.exec())
