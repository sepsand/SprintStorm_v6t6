"""
    Book class

    Extends the Reference class
    Contains additional fields:
        - publisher
        - address
"""
from src.references.reference import Reference

class Book(Reference):
    """
        Class for book references, extends Reference
    """
    def __init__(self, fields):
        super().__init__(
            fields={"author":fields['author'],
                    "title":fields['title'],
                    "year":fields['year']})
        self._publisher = fields['publisher']
        self._address = fields['address']

    @property
    def publisher(self):
        """
        Returns the publisher
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """
        Sets the publisher
        """
        self._publisher = publisher

    @property
    def address(self):
        """
        Return address
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets address
        """
        self._address = address