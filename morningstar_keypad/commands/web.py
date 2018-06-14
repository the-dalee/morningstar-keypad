import requests

from commands.core import Command


class HttpRequestCommand(Command):
    def __init__(self, url, method='GET', headers=None, data=None, hooks=None):
        self.hooks = hooks
        self.data = data
        self.headers = headers
        self.url = url
        self.method = method

    def execute(self):
        requests.request(method=self.method,
                         url=self.url,
                         headers=self.headers,
                         data=self.data,
                         hooks=self.hooks)


def http_request(url, method='GET', headers=None, data=None, hooks=None):
    return HttpRequestCommand(url, method=method,headers=headers, data=data,
                              hooks=hooks)
