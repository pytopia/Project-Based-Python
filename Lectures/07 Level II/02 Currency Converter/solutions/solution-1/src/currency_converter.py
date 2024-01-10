import requests
from functools import cache


# Function to get the exchange rate
@cache
def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]


# Function to convert the currency
def convert_currency(amount, exchange_rate):
    return amount * exchange_rate


if __name__ == '__main__':
    exchange_rate = get_exchange_rate("USD", "EUR")
    print(f"Exchange Rate: {exchange_rate}")
    usd_amount = 100
    eur_amount = convert_currency(usd_amount, exchange_rate)
    print(f"{usd_amount} USD is {eur_amount} EUR")
