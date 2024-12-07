import sys
from convert_text_to_audio import text_to_audio_local
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout,
    QLineEdit, QComboBox, QMessageBox, QWidget, QLabel, QProgressDialog
)
from PyQt6.QtCore import Qt


class TextToAudioApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text to audio")
        self.setGeometry(100, 100, 400, 200)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout(central_widget)

        # Input file selection
        self.file_input = QLineEdit(self)
        self.file_input.setPlaceholderText("Sélectionnez un fichier texte...")
        self.file_input.setReadOnly(True)
        file_button = QPushButton("Parcourir")
        file_button.clicked.connect(self.select_file)

        # Destination folder selection
        self.folder_input = QLineEdit(self)
        self.folder_input.setPlaceholderText("Sélectionnez un dossier de destination...")
        self.folder_input.setReadOnly(True)
        folder_button = QPushButton("Parcourir")
        folder_button.clicked.connect(self.select_folder)

        # Combo box
        self.combo_box = QComboBox(self)
        self.combo_box.addItems(["fr", "en"])  # Remplissez cette liste avec vos options

        # Generate button
        generate_button = QPushButton("Générer")
        generate_button.clicked.connect(self.generate)

        # Add widgets to layout
        layout.addWidget(QLabel("Fichier d'entrée :"))
        layout.addWidget(self.file_input)
        layout.addWidget(file_button)
        layout.addWidget(QLabel("Dossier de destination :"))
        layout.addWidget(self.folder_input)
        layout.addWidget(folder_button)
        layout.addWidget(QLabel("Choix :"))
        layout.addWidget(self.combo_box)
        layout.addWidget(generate_button)

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Sélectionnez un fichier texte", "", "Fichiers texte (*.txt);;Tous les fichiers (*)")
        if file_name:
            self.file_input.setText(file_name)

    def select_folder(self):
        folder_name = QFileDialog.getExistingDirectory(self, "Sélectionnez un dossier")
        if folder_name:
            self.folder_input.setText(folder_name)

    def generate(self):
        file_path = self.file_input.text()
        file_output_path = file_path.split(".")[0].split("/")[-1]
        folder_path = self.folder_input.text()
        choice = self.combo_box.currentText()
        file_output=f"{folder_path}/{file_output_path}.wav"

        print(f"Fichier sélectionné : {file_path}")
        print(f"Dossier de destination : {folder_path}")
        print(f"Fichier de sortie: {file_output}")
        print(f"Choix : {choice}")

        text_to_audio_local(file_path, file_output, choice, self.handle_state)
        QApplication.processEvents()  # Permet à l'UI de répondre pendant le chargement


    def handle_state(self, state: str):
        if state == "loading":
            self.progress = QProgressDialog("Chargement en cours...", None, 0, 0, self)
            self.progress.setWindowModality(Qt.WindowModality.ApplicationModal)
            self.progress.setCancelButton(None)
            self.progress.show()

        elif state == "success":
            if hasattr(self, "progress"):
                self.progress.close()
            QMessageBox.information(self, "Succès", "L'opération a été réalisée avec succès.")

        elif state == "error":
            if hasattr(self, "progress"):
                self.progress.close()
            QMessageBox.critical(self, "Erreur", "Une erreur s'est produite pendant l'opération.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextToAudioApp()
    window.show()
    sys.exit(app.exec())
