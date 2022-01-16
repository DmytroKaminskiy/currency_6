from sanic import Sanic
from sanic.response import json
import httpx
import requests

app = Sanic("Hello")


@app.route('/')
async def test(request):

    url = 'https://pythontutor.com/'
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        print(r.status_code)
    # requests.get(url)
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run(host="0.0.0.0")
