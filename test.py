import json
from datetime import datetime, date
from resources.tt import tt

today = datetime.today().strftime("%A")

text = f"{today}({date.today()})\n"
for period in tt[today]:
    text += tt[today][period]
    text += "\n"

print(text)