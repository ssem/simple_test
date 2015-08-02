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

if __name__ == "__main__":
    example = Example()
    print example.get_headers()
