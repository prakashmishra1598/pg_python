import requests
from scrapy.http.response.html import HtmlResponse
import logging

"""
Response = HTMLReponse of requests.get
"""
MAX_NUM_RETRY = 3


def get_response(url, headers=None, cookies=None, delay=30):
    num_retries = 0
    response = None
    if cookies is None:
        cookies = {}
    while num_retries < MAX_NUM_RETRY:
        try:
            response = None
            if headers is not None:
                response = requests.get(url, headers=headers,timeout=delay, verify=False, cookies=cookies)
            else:
                response = requests.get(url, timeout=delay, verify=False, cookies=cookies)
            num_retries += 1
            if response.status_code >= 200:
                ret_obj = HtmlResponse(url, status=response.status_code, body=response.body, encoding='utf-8')
                return ret_obj
        except Exception as e:
            logging.debug("Exception %s" %e.message)
            num_retries += 1
    logging.error("Could not fetch the url")
    err_obj = HtmlResponse(url, status=110, body="<html><body>Failure</body></html>", encoding='utf-8')
    return err_obj


if __name__ == "__main__":
    for i in range(0, 100):
        r = get_response('https://eprocure.gov.in/cppp/latestactivetenders', 60)
        logging.info(r.status)


