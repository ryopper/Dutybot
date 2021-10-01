import json
import datetime
import pandas as pd


dt_now = datetime.datetime.now()

file = open("info.json","r")
info = json.load(file)

from linebot import LineBotApi
from linebot.models import TextSendMessage

CHANNEL_ACCESS_TOKEN = info["CHANNEL_ACCESS_TOKEN"]
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

chart_duty = pd.read_csv("楓Duty.csv")

def main():
    USER_ID = info["USER_ID"]
    name = chart_duty.iloc[dt_now.day,1]
    messages = TextSendMessage(text = f"今日のDutyは{name}です。")
    line_bot_api.push_message(USER_ID, messages=messages)
    
if __name__ == "__main__":
    main()
