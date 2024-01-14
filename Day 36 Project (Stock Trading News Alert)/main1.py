import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

AV_API_KEY = "FDL4K1WQ28J67Y26"
AV_API_KEY1 = "XAJCR1FUWWQ37QKC"
newsapi = "5f58da60741c4d69aa417389b27d746a"

account_sid = "ACc931465dae26952f7c1ec6001c7718c0"
auth_token = "fd479c2fafb43bfc019a0eaa07af0f73"

my_twilio_phone = "+12019925595"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

av_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'IBM',
    'output_size': 'compact',
    'apikey': AV_API_KEY,
}

av_url = 'https://www.alphavantage.co/query?'
r = requests.get(av_url, params=av_parameters)
av_data = r.json()

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

av_list = [value for (key, value) in av_data["Time Series (Daily)"].items()]

yesterday_close = float(av_list[0]['4. close'])

#TODO 2. - Get the day before yesterday's closing stock price

day_bef_yesterday_close = float(av_list[1]['4. close'])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
pos_diff = abs(yesterday_close - day_bef_yesterday_close)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = round((pos_diff/((yesterday_close + day_bef_yesterday_close)/2)) * 100, 2)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if percentage_diff > 5:
    news_params = {
        'apiKey': newsapi,
        'q': COMPANY_NAME,
        'page': 1,


    }
    news_url = "https://newsapi.org/v2/everything"
    r = requests.get(news_url, params=news_params)

    news_data = r.json()

    news_list = [news for news in news_data['articles']]

    first_three_news = news_list[:3]

# for i in first_three_news:
#     print(i['title'])
#     print(i['description'])


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    news_hl_desc = [[i['title'], i['description']] for i in first_three_news]
    print(news_hl_desc)


#TODO 9. - Send each article as a separate message via Twilio.

    for i in news_hl_desc:
        client = Client(account_sid, auth_token)
        message = client.messages\
            .create(
                body=f"{STOCK_NAME}: {percentage_diff}%\nHeadline: {i[0]}\nBrief: {i[1]}",
                from_='+12019925595',
                to='+639761214776'
            )
        print(message.status)

else:
    print("No way")


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

