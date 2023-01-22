import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
FUNC = "TIME_SERIES_DAILY_ADJUSTED"
STOCK_API_URL = "https://www.alphavantage.co/query"
NEWS_API_URL = "https://newsapi.org/v2/everything"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_API_KEY = os.environ.get("TWILIO_API_KEY")


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def check_price_diff(prices):
    """
    Check the price diff of given prices
    :param prices:
    :return:
    """
    pct_diff = abs(prices[0] - prices[1])/prices[0] * 100
    return pct_diff


def get_prices(stock):
    """
    Takes a stock as input and gets the last 2 closing prices. Returns them as a list
    :param stock:
    :return:
    """
    stock_params = {
        "function": FUNC,
        "symbol": stock,
        "apikey": STOCK_API_KEY,
        "outputsize": "compact"
    }
    stock_request = requests.get(STOCK_API_URL, params=stock_params).json()
    # print(stock_request)

    stock_daily_data = stock_request.get("Time Series (Daily)")
    # print(stock_daily_data)

    last_two_days = [float(day[1].get("4. close")) for day in list(stock_daily_data.items())[:2]]
    return last_two_days


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_news(company_name):
    """
    Given a company name, gets the last 3 news articles for the company and returns them as a list
    :param company_name:
    :return:
    """
    news_params = {
        "qInTitle": company_name,
        "from": "date",
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }
    news_request = requests.get(NEWS_API_URL, params=news_params).json()
    articles = news_request.get("articles")[:3]
    return articles


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_twilio(msg):
    client = Client(TWILIO_SID, TWILIO_API_KEY)
    message = client.messages.create(
        body=msg,
        from_="TwilioPhoneNumber",
        to="YourNumber"
    )
    print(message.status)


def get_emoji(price_1, price_2):
    if price_1 - price_2 < 0.0:
        return "🔻"
    return "🔺"

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

if __name__ == "__main__":

    stock = STOCK
    company_name = COMPANY_NAME

    prices = get_prices(stock)
    emoji = get_emoji(prices[0], prices[1])
    pct_diff = check_price_diff(prices)

    if pct_diff > 0.8:
        article_list = get_news(company_name)
        for article in article_list:
            msg = f"{stock}: {emoji}{round(pct_diff)}%\nHeadline: {article.get('title')}\nBrief: {article.get('description')}"
            send_twilio(msg)
