import requests
import json

def get_quotes():
    headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
                }

    try:
        quote_page = requests.get('https://api.quotable.io/random', headers = headers)
    except:
        return False, ""

    quote_page = quote_page.text
    quote_page = json.loads(quote_page)

    quote = quote_page["content"]
    author = quote_page["author"]
    text = ""
    text += quote
    text += "\n- "
    text += author

    return True, text