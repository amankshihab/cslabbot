import json
from datetime import datetime, date
from resources.tt import tt


today = datetime.today().strftime("%A")

text = f"**{today}({date.today()})**\n\n"
for period in tt[today]:
    text += "__"
    text += tt[today][period]
    text += "__"
    text += "\n"

print(text)