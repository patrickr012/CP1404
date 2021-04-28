"""
Patrick Robinson
12251568
CP1404
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Main Program - Kivy app to demonstrate box layouts"""
    def build(self):
        """Build the Kivy GUI"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Creating the greeting label and modifying it based on user input"""
        print("Greet")

        self.root.ids.output_label.text = "Hello, " + self.root.ids.input_name.text

    def clear_text(self):
        """Clearing the input box and greeting label on button press"""
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""

BoxLayoutDemo().run()
