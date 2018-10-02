#!/usr/bin/env python3
import unittest


class Todo:
    def __init__(self):
        self._text: str = None
        self._author: str = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        self._author = author


class TestSolution(unittest.TestCase):
    def test_property_success(self):
        todo = Todo()
        todo.text = 'todo-1'
        todo.author = 'author-1'

        self.assertEqual('todo-1', todo.text)
        self.assertEqual('author-1', todo.author)


if __name__ == '__main__':
    unittest.main()
