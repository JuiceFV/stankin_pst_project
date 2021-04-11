"""This file contains the wrapper for tinder API. The most of code has been copied from pynder package
(https://github.com/charliewolf/pynder.) However I've enhanced this package by adding the proper facebook authorization.
Also I've adapted pynder for my own purposes by getting rid of some redundant (to me of course) methods.
"""
import requests
import json
import threading
import application.sources.tinder_api.globals as constants
from application.sources.tinder_api.facebook_auth import get_facebook_access_token
import application.sources.tinder_api.exceptions as errors

__all__ = ('TinderAPI',)


class TinderAPI:
    """The base API class, methods of this class interacts with tinder API
    """

    def __init__(self, x_auth_token=None):
        """
        The constructor of the TinderAPI class, it is initializing a session.
        :param x_auth_token: if an user somehow retrieved XAuthToken, he could pass it. (None by default)
        """
        self._session = requests.Session()
        self._session.headers.update(constants.HEADERS)
        self._x_auth_token = x_auth_token

        # If an user passed a XAuthToken it should be updated in headers dict.
        if self._x_auth_token:
            self._session.headers.update({'Authorization': "Token token='#{'" + str(self._x_auth_token) + "'}'"})
            self._session.headers.update({'X-Auth-Token': str(self._x_auth_token)})

    @staticmethod
    def _tie_link(end_point):
        """The method which helps to create proper URL.
        :param end_point: the endpoint of a requested link.
        :return: built up link
        """
        _url = end_point.lower()

        # In case if passes entire link then returns itself
        if _url.startswith("http://") or _url.startswith("https://"):
            return end_point
        # However if passes endpoint then builds integral link and returns it.
        else:
            return constants.HOST + end_point

    def _get_xauth_token(self, fb_auth_token):
        """In most of case use this method to retrieve a XAuthToken.
        :param fb_auth_token: the authentication token obtained from facebook using your fb email and fb password.
        :return: either a token nor None if token is missing.
        """
        response = self._session.request(
            constants.KEY_ENDPOINTS['fb_auth']['method'],
            constants.HOST + constants.KEY_ENDPOINTS['fb_auth']['endpoint'],
            headers={'app_version': '11', 'platform': 'ios', 'content-type': 'application/json'},
            data=json.dumps({'token': fb_auth_token}),
            timeout=1,
        )
        try:
            return response.json()['data']['api_token']
        except:
            return None

    def auth(self, facebook_email, facebook_password):
        """Method performs authentication an user in tinder.
        :param facebook_email: user's facebook email
        :param facebook_password: user's facebook password
        """
        if self._x_auth_token is None:
            # If a XAuthToken hasn't passed, yet I retrieve a token using fb password and fb email.
            self._x_auth_token = self._get_xauth_token(get_facebook_access_token(facebook_email, facebook_password))
            if self._x_auth_token is None:
                raise errors.InitializationError("Authorization has been wrong. Couldn't retrieve a tinder's token.\n"
                                                 "Check if your facebook's email and password are precise.")
            self._session.headers.update({'Authorization': "Token token='#{'" + str(self._x_auth_token) + "'}'"})
            self._session.headers.update({'X-Auth-Token': str(self._x_auth_token)})

    def _request(self, method, end_point, data={}):
        """Basically this method is the wrapper for any request.
        :param method: the method of a request (GET, POST, DELETE, UPDATE)
        :param end_point: the endpoint all endpoints are presented here https://github.com/fbessez/Tinder
        :param data: possible request data. (dict() by default)
        :return: response in json format
        """
        if self._x_auth_token is None:
            raise errors.InitializationError
        response = self._session.request(method, self._tie_link(end_point), data=data)
        while response.status_code == 429:
            blocker = threading.Event()
            blocker.wait(0.1)
            response = self._session.request(method, self._tie_link(end_point), data=data)
        if response.status_code < 200 or response.status_code >= 300:
            raise errors.RequestError(response.status_code)
        if response.status_code == 201 or response.status_code == 204:
            return {}
        return response.json()

    def _get(self, url):
        """Wrapper for get request
        :param url: a requested link
        :return: response
        """
        return self._request("get", url)

    def _post(self, url, data={}):
        """Wrapper for post request
        :param url: a requested link
        :param data: possible request data. (dict() by default)
        :return: response
        """
        return self._request("post", url, data=data)

    def _delete(self, url):
        """Wrapper for delete request
        :param url: a requested link
        :return: response"""
        return self._request("delete", url)
