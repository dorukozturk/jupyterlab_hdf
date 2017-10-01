import requests
import urlparse
from notebook.base.handlers import IPythonHandler


class H5ServClient(object):
    def __init__(self):
        self.h5serv_url = 'http://localhost:5000'

    def _proxy(self, method, path, *args, **kwargs):
        url = urlparse.urljoin(self.h5serv_url, path[4:])
        return method(url, *args, **kwargs).json()

    def get(self, path, *args, **kwargs):
        return self._proxy(requests.get, path, *args, **kwargs)

class HdfHandler(IPythonHandler):
    def get(self):
        client = H5ServClient()
        self.finish(client.get(self.request.uri))
