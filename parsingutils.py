import requests
import re
import math

BASE_URL = 'https://news.ycombinator.com/'
ITEMS_PER_PAGE = 30


def get_page(page: int = 1) -> str:
    """Returns html of specified hacker news feed `page`"""
    assert page >= 1

    url = BASE_URL
    if page > 1:
        url = f'{BASE_URL}?p={page}'

    return requests.get(url).text


def parse_page(html: str):
    pattern = r'rank">(?P<rank>\d+)\..*?<a\s+href="(?P<url>[^"]+)"\sclass="storylink">(?P<title>[^<]+)<.*?(?P<points>\d+)\spoints.*?nuser">(?P<author>[^<]+).*?(?P<comments>\d+)&nbsp;comments'

    matches = []

    for m in re.finditer(pattern, html, re.I | re.M | re.S):
        matches.append(m.groupdict())

    return matches


def load_n_results(n: int = 10):
    numpages = math.ceil(n / ITEMS_PER_PAGE)
    html = ''

    for i in range(numpages):
        try:
            html += get_page(i + 1)
        except Exception as e:
            print(f'Failed to load page {i}')
            break

    return parse_page(html)[:n]
