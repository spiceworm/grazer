import concurrent.futures

import bs4
import requests
import yaml


def get_price(label, element):
    url = element["url"]
    css_selector = element["css_selector"]
    html_key = element.get("html_key")

    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, features="html.parser")
    selected = soup.select(css_selector)[0]
    if html_key:
        result = selected.get(html_key)
    else:
        result = selected.text
    return {label: result}


def graze(config: str | None = None, elements: dict | None = None):
    _elements = elements or {}
    if config:
        with open(config) as f:
            _elements.update(yaml.safe_load(f))

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(get_price, label, element) for label, element in _elements.items()]
        yield from (f.result() for f in concurrent.futures.as_completed(futures))
