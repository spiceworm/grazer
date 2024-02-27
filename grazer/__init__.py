import aiohttp
import asyncio

import bs4
import yaml


async def consumer(q):
    while True:
        try:
            yield await asyncio.wait_for(q.get(), 5)
        except (asyncio.QueueEmpty, asyncio.TimeoutError):
            break


async def worker(label, element, session, q):
    url = element["url"]
    css_selector = element["css_selector"]
    html_key = element["html_key"]

    async with session.get(url) as resp:
        if resp.ok:
            text = await resp.read()
            soup = bs4.BeautifulSoup(text, features="html.parser")
            selected = soup.select(css_selector)
            result = selected[0].get(html_key)
            await q.put({label: result})


async def execute(elements: dict):
    q = asyncio.Queue(maxsize=0)

    async with aiohttp.ClientSession() as session:
        tasks = []
        for label, element in elements.items():
            task = asyncio.create_task(worker(label, element, session, q))
            tasks.append(task)

        async for result in consumer(q):
            print(result)

        await asyncio.gather(*tasks)


def graze(config: str | None = None, elements: dict | None = None):
    _elements = elements or {}
    if config:
        with open(config) as f:
            _elements.update(yaml.safe_load(f))

    import time
    start = time.time()
    asyncio.run(execute(_elements))
    print(f'ran in {time.time() - start} seconds')
