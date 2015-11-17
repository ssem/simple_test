#!/usr/bin/env python
import requests

class Example():
    def __init__(self):
        self.test = 'test assignment'

    def get_headers(self):
        http = requests.get(
            url='http://www.google.com',
            timeout=5)
        return http.headers

    def parameters(self, number=1):
        self._parameters(number, "a", "foo bar")

    def parameters_called_twice(self, number=1):
        self._parameters(number, "a", "foo bar")
        self._parameters(1, "a", "foo bar")

    def _parameters(self, number, char, string):
        return 0

if __name__ == "__main__":
    example = Example()
    print example.get_headers()
