# /usr/bin/env python
# -*- coding:utf8 -*-

from requests import Request, Session
from urllib.parse import urljoin
import json
import random
from urllib import parse as urlparse
import requests
import string


BASE_URL = "https://merchant.wish.com/"
BASE_SANDBOX_URL = "https://sandbox.merchant.wish.com/"
BASE_ENDPOINT = "api/v2/"

class Resource(object):
    def __init__(self, client):
        self.client = client


def list(self, **kwargs):
        """
        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/product/multi-get


        :param kwargs:
        :return:
        """
        return self.client.execute("product/multi-get", "GET", kwargs)

def update(self, update_data):
        """
        HTTP Request Type: POST
        
        Definition
        POST https://merchant.wish.com/api/v2/product/update
        :param update_data:
        :return:
        """
        return self.client.execute("product/update", "POST", update_data)

def retrieve(self, **kwargs):
        """
        HTTP Request Type: GET

        Definition
        GET https://merchant.wish.com/api/v2/product
        :param kwargs:
        :return:
        """
        return self.client.execute("product", "GET", kwargs)

def build_url(self, uri):
        return urljoin(self.base_url, uri)

def execute(self, uri, method, body):
        method = method.upper()
        req = self.build_request(uri, method, body)
        prepped = req.prepare()
        s = Session()
        resp = s.send(prepped)
        resp = build_response(resp)
        return resp

def build_request(self, uri, method, body):
        url = self.build_url(uri)
        headers = {
            "Authorization": "Bearer " + self.access_token
        }

        req = Request(method, url, headers=headers)

        if body:
            if req.method in ["POST", "PUT", "PATH"]:
                req.data = body
            else:
                req.params = body
        return req

import json


def build_response(resp):
    b = json.loads(resp.text)
    if resp.status_code == 200 and b["code"] == 0:
        if "data" in b:
            return b["data"]
        return b
    raise ValueError(b['message'])


__all__ = ["Oauth"]


class Oauth(object):
    authorization_endpoint = "/oauth/authorize"
    access_token_endpoint = BASE_ENDPOINT.rstrip("/") + "/oauth/access_token"
    refresh_token_endpoint = BASE_ENDPOINT.rstrip("/") + "/oauth/refresh_token"

    def __init__(self, client_id, client_secret, redirect_uri, env="PROD"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

        if env == "SANDBOX":
            self.base_authorization_url = urlparse.urljoin(BASE_SANDBOX_URL, self.authorization_endpoint)
            self.base_access_token_url = urlparse.urljoin(BASE_SANDBOX_URL, self.access_token_endpoint)
            self.base_refresh_token_url = urlparse.urljoin(BASE_SANDBOX_URL, self.access_token_endpoint)
        else:
            self.base_authorization_url = urlparse.urljoin(BASE_URL, self.authorization_endpoint)
            self.base_access_token_url = urlparse.urljoin(BASE_URL, self.access_token_endpoint)
            self.base_refresh_token_url = urlparse.urljoin(BASE_URL, self.refresh_token_endpoint)

    def make_authorization_url(self, state=None, scope=None):
        u = urlparse.urlparse(self.base_authorization_url)
        if not state:
            state = "".join(random.sample(string.ascii_letters, 32))
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "state": state
        }
        if scope:
            params["scope"] = " ".join(scope)

        query = urlparse.urlencode(params)

        url = urlparse.urlunparse((u.scheme, u.netloc, u.path, u.params, query, u.fragment))
        return url, state



    def get_access_token(self, authorization_code):
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": authorization_code,
            'grant_type': 'authorization_code',
            'redirect_uri': self.redirect_uri
        }
        r = requests.post(self.base_access_token_url, data=params)
        return build_response(r)

    def get_access_token_by_refresh_token(self, refresh_token):
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": refresh_token,
            'grant_type': 'refresh_token'
        }
        r = requests.post(self.base_refresh_token_url, data=params)
        return build_response(r)

