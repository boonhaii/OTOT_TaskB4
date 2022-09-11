import json
import requests

currencies_in_asia = [
    'AED',
    'AFN',
    'AMD',
    'AUD',
    'AZN',
    'BDT',
    'BHD',
    'BND',
    'BTN',
    'CNY',
    'EUR',
    'GEL',
    'HKD',
    'IDR',
    'ILS',
    'INR',
    'IQD',
    'IRR',
    'JOD',
    'JPY',
    'KGS',
    'KHR',
    'KPW',
    'KRW',
    'KWD',
    'KZT',
    'LAK',
    'LBP',
    'LKR',
    'MMK',
    'MNT',
    'MOP',
    'MVR',
    'MYR',
    'NPR',
    'OMR',
    'PHP',
    'PKR',
    'QAR',
    'RUB',
    'SAR',
    'SGD',
    'SYP',
    'THB',
    'TJS',
    'TMT',
    'TRY',
    'TWD',
    'USD',
    'UZS',
    'VND',
    'YER'
 ]

def lambda_handler(event, context):
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    data = response.json()
    asian_currencies_rates = {}
    available_rates = data["rates"].keys()
    for currency in currencies_in_asia:
        if currency in available_rates:
            asian_currencies_rates[currency] = data["rates"][currency]
    
    return {
        "base": data["base"],
        "rates": asian_currencies_rates
    }
