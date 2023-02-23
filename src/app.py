import os
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("フォルダ作成")
        self.setGeometry(100, 100, 400, 200)

        self.year_label = QLabel("対象の年を入力してください（例：2022）", self)
        self.year_label.move(20, 20)
        self.year_label.adjustSize()

        self.year_textbox = QLineEdit(self)
        self.year_textbox.move(20, 50)
        self.year_textbox.resize(280, 40)

        self.folder_label = QLabel("保存先を選択してください", self)
        self.folder_label.move(20, 100)
        self.folder_label.adjustSize()

        self.folder_button = QPushButton("選択", self)
        self.folder_button.move(20, 130)
        self.folder_button.clicked.connect(self.select_folder)

        self.create_button = QPushButton("作成", self)
        self.create_button.move(20, 170)
        self.create_button.clicked.connect(self.create_folders)

        self.selected_folder = ""

    def select_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        self.selected_folder = QFileDialog.getExistingDirectory(
            self, "保存先を選択", options=options)
        if self.selected_folder:
            self.folder_label.setText(f"保存先：{self.selected_folder}")
            self.folder_label.adjustSize()

    def create_folders(self):
        year = self.year_textbox.text()
        if not self.selected_folder:
            self.folder_label.setText("保存先を選択してください")
            self.folder_label.adjustSize()
            return
        for month in range(1, 13):
            folder_name = f"{year}-{month:02}"
            full_path = os.path.join(self.selected_folder, folder_name)
            if not os.path.exists(full_path):
                os.mkdir(full_path)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
