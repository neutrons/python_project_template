"""
Main Qt window
"""

from qtpy.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QTabWidget, QPushButton

from packagenamepy.presenters.main import MainPresenter
from packagenamepy.models.main import MainModel
from packagenamepy.views.main import Main

from packagenamepy.models.help import help_function


class MainWindow(QWidget):
    """Main widget"""

    def __init__(self, parent=None):
        super().__init__(parent)

        ### Create tabs here ###

        ### Main tab
        self.tabs = QTabWidget()
        main = Main(self)
        main_model = MainModel()
        self.main_presenter = MainPresenter(main, main_model)
        self.tabs.addTab(main, "Main")
        

        ### Set tab layout
        layout = QVBoxLayout()
        layout.addWidget(self.tabs)


        ### Create bottom interface here ###
        
        # Help button
        help_button = QPushButton("Help")
        help_button.clicked.connect(self.handle_help)


        # Set bottom interface layout
        hor_layout = QHBoxLayout()
        hor_layout.addWidget(help_button)

        layout.addLayout(hor_layout)

        self.setLayout(layout)

        # register child widgets to make testing easier
        self.main = main

    def handle_help(self):
        """
        get current tab type and open the corresponding help page
        """
        open_tab = self.tabs.currentWidget()
        if isinstance(open_tab, Main):
            context = "main"
        else:
            context = ""
        help_function(context=context)
