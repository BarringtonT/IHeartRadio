#!/usr/bin/env python3
'''
Created on Sep 3, 2014

@author: boss
'''

from urllib.error import URLError, HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


url = input('Please enter web address')
req = Request(url)
