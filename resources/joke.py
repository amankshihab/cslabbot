import requests
import json

headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }

joke_page = requests.get('https://official-joke-api.appspot.com/random_joke', headers = headers)
joke_page = joke_page.text
joke_page = json.loads(joke_page)

joke = joke_page["setup"]
joke += "\n"
joke +=  joke_page["punchline"]