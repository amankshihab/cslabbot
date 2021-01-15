import requests
import json

def get_joke():
    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }

    try:
        joke_page = requests.get('https://official-joke-api.appspot.com/random_joke', headers = headers)
    except:
        return False, "none"

    joke_page = joke_page.text
    joke_page = json.loads(joke_page)

    joke = joke_page["setup"]
    joke += "\n\n"
    joke +=  joke_page["punchline"]

    return True, joke