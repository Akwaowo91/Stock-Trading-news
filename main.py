import requests
from twilio.rest import Client

TWILIO_ACCOUNT_SID = "AC8d7b8210b1e5850ad6598977666de3bd"
TWILIO_AUTH_TOKEN = "e51799d13d6e495b4d60c6db1f0028b5"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key = "G7L37RK0YSLWM6E2"
news_api_key = "a0f201a2025c4bfaafceb4513c38e71b"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()['Time Series (Daily)']

stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(f"This is the closing price 1 days ago:{yesterday_closing_price}")

# Get the day before yesterday's closing stock price

day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(f"This is the closing price 2 days ago:{day_before_yesterday_closing_price}")

# Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.

positive_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
# print(f"This is the positive difference from the past 2 days:{positive_difference}")

up_down = None
if positive_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday
percentage_difference = round((positive_difference / float(yesterday_closing_price)) * 100)
# print(f"This is the current percentage difference:{percentage_difference}")


## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# If TODO4 percentage is greater than 5 then print("Get News").
if abs(percentage_difference) > 1:
    news_params = {
        "q": COMPANY_NAME,
        "sortBy": "popularity",
        "apikey": news_api_key
    }

    response_news = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = response_news.json()["articles"]

    # Use Python slice operator to create a list that contains the first 3 articles.

    three_news_article = news_data[:3]
    # print(three_news_article)

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python

    # Create a new list of the first 3 articles headline and description using list comprehension.
    news_article_info = [
        f"{STOCK_NAME}: {up_down}{percentage_difference} %\nHeadlines: {article['title']}. \nBrief: {article['description']} "
        for article in three_news_article]
    print(news_article_info)

    # to send a separate message with each article's title and description to your phone number.
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for article in news_article_info:
        message = client.messages.create(
            body=article,
            from_="+18665038545",
            to="+17015008460"
        )
