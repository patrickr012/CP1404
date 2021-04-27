"""
Patrick Robinson
12251568
CP1404
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder




class DynamicLabels(App):
    """ Main Program - Kivy app to demonstrate dynamic labels"""

    def __init__(self, **kwargs):
        """Constructing the main app"""
        super().__init__(**kwargs)
        self.nato_alphabet = ("Alpha", "Bravo", "Charlie")


    def build(self):
        """Building the Kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root


    def create_widgets(self):
        """Creating labels based on list entries"""
        for entry in self.nato_alphabet:

            dynamic_label_display = Label(text = entry)
            self.root.ids.label_box.add_widget(dynamic_label_display)


DynamicLabels().run()
