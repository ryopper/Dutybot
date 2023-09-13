import json
import datetime
import pandas as pd
import requests

dt_now = datetime.datetime.now()

file = open("info_slack.json","r")
info = json.load(file)


CHANNEL = info["CHANNEL"]
TOKEN = info["TOKEN"]
URL = info["URL"]

chart_duty = pd.read_excel("新DUTY_LIST.xlsx")

def main():
    name = chart_duty.iloc[dt_now.day,1]
    if pd.isnull(name) == False:
        text = f'*本日のDutyは{name}さんです。*'
        data = {
            'token': TOKEN,
            'channel': CHANNEL,
            'text': text
        }
        response = requests.post(URL, data=data)


if __name__ == "__main__":
    main()
