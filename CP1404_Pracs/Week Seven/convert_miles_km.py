"""
Patrick Robinson
12251568
Program for converting miles into kilometers
CP1404
"""
MILES_COEFFIENT = 1.609
from kivy.app import App
from kivy.lang import Builder

class MilesConverter(App):
    """A Kivy App designed to convert miles into kilometers"""
    def build(self):
        """Building the Kivy GUI"""
        self.title = "Miles Converter"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate_kilometers(self):
        """Converting the input into kilometers, converting it into a string and outputting it to a label"""
        checked_miles_input = self.check_miles_input()
        kilometers_amount = checked_miles_input * MILES_COEFFIENT
        self.root.ids.output_label.text = str(kilometers_amount) + " Kilometers"



    def handle_increment(self, increment_value):
        """Increasing or decreasing the input number value by 1, depending on the button pressed
            :param increment_value: the number passed from the up or down buttons"""
        initial_value = self.check_miles_input()
        new_value = int(initial_value) + int(increment_value)
        self.root.ids.input_number.text = str(new_value)

    def check_miles_input(self):
        """Checking the input, defaulting to zero if the value is invalid"""
        try:
            miles_input = float(self.root.ids.input_number.text)
            return miles_input
        except ValueError:
            return 0




MilesConverter().run()

