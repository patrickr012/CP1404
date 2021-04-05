"""
Patrick Robinson
12251568



"""


class ProgrammingLanguage:
    """Represent a programming language object.


    """

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a programming language instance.

        typing: string, indicates whether the program has dynamic or static typing
        reflection: boolean, indicated whether the program has reflection or not
        year: int, the year the program was invented
        name: string, the name of the program

        """
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.name = name

    def is_dynamic(self):
        """ Checking if 'Dynamic' appears in the object.  Returning true if so.


        """
        if "Dynamic" in self.typing:
            return "True"

    def __str__(self):
        """Printing the object in a formatted form.



        """
        return f'{self.name}, {self.typing} typing, Reflection={self.is_dynamic()}, First appeared in {self.year}'
