from urlparse import urljoin


"""
For every service we need to define
(a) protocol
(b) ip or base_domain (including subdomain) e.g. red.blue.com, 104.89.45.66
(c) port (if 80, still define it), must be an integer
"""

import logging

_protocol_http_ = "http://"
_protocol_https_ = "https://"

allowed_protocols = [_protocol_http_, _protocol_https_]

class ServiceEndpoint(object):

    def __init__(self, protocol, base_addr, port):
        self.protocol = protocol
        self.base_addr = base_addr
        self.port = port
        self._make_endpoint()

    def _make_endpoint(self):
        # validate
        if type(self.port) is not int:
            logging.error("Port is not defined as integer")
            self.endpoint = None
            return
        if self.protocol not in allowed_protocols:
            logging.error("Protocol incorrect, please use http:// or https://")
            return
        if (self.port < 9000) or (self.port > 9999):
            logging.warn("Port range is not as expected for us %s " % self.port)
        self.endpoint = self.protocol + self.base_addr + ":" + str(self.port) + "/"

    def get_endpoint(self):
        return self.endpoint

##### service endpoints are below #####
nodejs_ip = "crawler-1.hawker.news"
nodejs_port = 9001
nodejs_service_obj = ServiceEndpoint(_protocol_http_, nodejs_ip, nodejs_port)
nodejs_service_url = nodejs_service_obj.get_endpoint()
