#! /usr/bin/env python3
"""internet_on.py
Checks to make sure that an internet connection is present before
the rest of a script will run."""


import urllib.request
import time


class NoInternetError(Exception):
    '''Error for no internet connectivity.'''
    pass


def internet_on():
    google_url = 'http://74.125.228.100'

    for x in range(6):
        try:
            response = urllib.request.urlopen(google_url, timeout=1)
            return True
        except urllib.error.URLError as err:
            time.sleep(5)
    raise NoInternetError('There was no internet connectivity when I tried to '
                          'run at {}.'.format(time.asctime()))
