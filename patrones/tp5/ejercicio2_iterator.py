from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any

class StringIterator(Iterator):
   
    def __init__(self, string: str, reverse: bool = False) -> None:
        self._string = string
        self._reverse = reverse
        self._position = len(string) - 1 if reverse else 0
    
    def __next__(self) -> str:
        if self._reverse and self._position < 0:
            raise StopIteration()
        if not self._reverse and self._position >= len(self._string):
            raise StopIteration()
        
        char = self._string[self._position]
        
        self._position += -1 if self._reverse else 1
        
        return char


class StringCollection(Iterable):
    def __init__(self, text: str) -> None:
        self._text = text

    def __iter__(self) -> StringIterator:
        return StringIterator(self._text, reverse=False)
        
    def get_reverse_iterator(self) -> StringIterator:
        return StringIterator(self._text, reverse=True)


if __name__ == "__main__":
    cadena = StringCollection("ingenieria")
    
    print("straight traversal:")
    for char in cadena:
        print(char, end=' ')
    print("\n")
    
    print("reverse traversal:")
    for char in cadena.get_reverse_iterator():
        print(char, end=' ')
    print("\n")