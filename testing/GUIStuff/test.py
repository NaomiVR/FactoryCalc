import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QScrollArea, QComboBox, QLabel,
                             QPushButton, QGridLayout, QFormLayout, QGroupBox,
                             QTreeWidget, QTreeWidgetItem)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Layout Dashboard")
        self.resize(1100, 700)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)

        # --- LEFT SIDE: Scrollable Icons ---
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.icon_container = QWidget()
        self.icon_layout = QGridLayout(self.icon_container)
        self.icon_layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Keep icons at the top
        self.scroll.setWidget(self.icon_container)
        layout.addWidget(self.scroll, stretch=3)

        # --- RIGHT SIDE: Control Panel ---
        right_panel = QVBoxLayout()

        # 1. Configuration Group (Replacing Text Area with Dropdowns)
        config_group = QGroupBox("Configuration Parameters")
        form_layout = QFormLayout()

        # Main Controller Dropdown
        self.category_combo = QComboBox()
        self.category_combo.addItems(["Architecture", "Nature", "Abstract"])
        self.category_combo.currentIndexChanged.connect(self.load_icons)
        form_layout.addRow(QLabel("Asset Category:"), self.category_combo)

        # Additional Dropdowns
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["Recent", "Alphabetical", "High Resolution"])
        form_layout.addRow(QLabel("Sort By:"), self.filter_combo)

        self.size_combo = QComboBox()
        self.size_combo.addItems(["Small (64px)", "Medium (128px)", "Large (256px)"])
        form_layout.addRow(QLabel("Icon Size:"), self.size_combo)

        config_group.setLayout(form_layout)
        right_panel.addWidget(config_group)

        # 2. Tree View (For Calculations/Hierarchy)
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Property", "Value"])
        self.setup_tree_data()
        right_panel.addWidget(QLabel("Selection Analysis:"))
        right_panel.addWidget(self.tree)

        # 3. Action Buttons
        self.win_btn = QPushButton("Launch Image Gallery Window")
        self.win_btn.setFixedHeight(40)
        self.win_btn.clicked.connect(self.open_image_window)
        right_panel.addWidget(self.win_btn)

        layout.addLayout(right_panel, stretch=1)

        # Initial Load
        self.load_icons()

    def setup_tree_data(self):
        """Creates dummy tree data."""
        parent = QTreeWidgetItem(self.tree, ["Selection Stats", ""])
        QTreeWidgetItem(parent, ["Total Selected", "0"])
        QTreeWidgetItem(parent, ["Total Weight", "0.00 kg"])
        self.tree.expandAll()

    def load_icons(self):
        """Clears and reloads icons based on the primary dropdown."""
        # Clear layout
        while self.icon_layout.count():
            child = self.icon_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        category = self.category_combo.currentText()
        # Create 24 toggleable icons
        for i in range(24):
            btn = QPushButton(f"{category[:3]} {i}")
            btn.setCheckable(True)
            btn.setFixedSize(100, 100)
            # Simple styling for the 'Checked' state
            btn.setStyleSheet("""
                QPushButton { border: 2px solid #ccc; border-radius: 5px; background: #f0f0f0; }
                QPushButton:checked { background-color: #3498db; color: white; border-color: #2980b9; }
            """)
            self.icon_layout.addWidget(btn, i // 4, i % 4)

    def open_image_window(self):
        print("Launching Image Window...")
        # This is where your second window logic would go


app = QApplication(sys.argv)
# Apply a modern look
app.setStyle("Fusion")
window = MainWindow()
window.show()
sys.exit(app.exec())