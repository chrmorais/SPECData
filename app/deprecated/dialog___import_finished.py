from PyQt4.QtCore import *
from PyQt4.QtGui import *

from app.dialogs.frames.manage_database.frame___import_finished import Ui_importfinished_frame  # Import Frame
from app.events import clickable


class ImportFinished(QDialog):
    def __init__(self, log_message):
        super(ImportFinished, self).__init__()
        self.ui= Ui_importfinished_frame()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.resize(1025, 750)

        self.log_message = log_message

        self.connect_buttons()  # Connect buttons to appropriate scripts
        self.display_log_message()  # Display Log Message to Screen

    def connect_buttons(self):
        # Get buttons/labels
        return_lbl = self.ui.return_lbl

        # Set Buttons
        clickable(return_lbl).connect(self.return_to_main_menu)

    def display_log_message(self):
        """
        Displays Log Message to Screen
        :return:
        """
        log_list = self.ui.log_list
        if self.log_message is not None:
            for line in self.log_message:
                item = QListWidgetItem(line)
                log_list.addItem(item)

    def return_to_main_menu(self):
        """
        Closes current window and returns to MainWindow
        :return:
        """
        from dialog___main_menu import MainMenu  # Next Window (Return to Menu)
        self.close()
        window = MainMenu()
        window.exec_()
