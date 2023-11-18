"""Module for the valid request type"""


class ValidRequest:
    """ClientListValidRequest"""

    def __init__(self, data):
        self.data = data

    def __bool__(self):
        return True
