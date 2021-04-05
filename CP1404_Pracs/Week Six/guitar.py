"""
Patrick Robinson
12251568

Creating the guitar class and its methods.

"""


class Guitar:
    """
    Represent a Guitar object


    """

    def __init__(self, name="", year=0, cost=0):
        """
        Parameters:
            name: string, indicates the name of the guitar
            year: int, the year the guitar was made
            cost: float, the cost of the guitar
            """
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """ Returning the age of the guitar, based on the year it was produced.


        """
        age = 2020 - self.year
        return age

    def is_vintage(self):
        """ Returning whether the guitar is vintage, based on its age.



        """
        if 2020 - self.year >= 50:
            return "True"
        else:
            return "False"

    def __str__(self):
        """Printing the object in a formatted form.



        """
        return f' Name:{self.name}, Year:{self.year} , worth:${self.cost}, age:{self.get_age()}, vintage:{self.is_vintage()}'
