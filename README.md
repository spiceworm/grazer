```python
import grazer

elements={
    'AAPL': {
        'css_selector': 'fin-streamer.Fw\\(b\\):nth-child(1)', 'html_key': 'value', 'url': 'https://finance.yahoo.com/quote/AAPL',
    },
    'AMZN': {
        'css_selector': 'fin-streamer.Fw\\(b\\):nth-child(1)', 'html_key': 'value', 'url': 'https://finance.yahoo.com/quote/AMZN',
    },
}

for result in grazer.graze(elements=elements):
    print(result)
# or
for result in grazer.graze(config="./example-config.yaml"):
    print(result)
```
