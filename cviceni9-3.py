from unittest.mock import MagicMock
import requests

def stahuj(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.content
    

def test_stahuj():
    assert