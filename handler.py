import json
import requests
import pprint

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
    try:
        if event != None and "body" in event:
            blob = event["body"]
            args = json.loads(blob)
            amount = 1
            if args["amount"] != None:
                amount = args["amount"]
            
            url = 'https://api.exchangerate.host/latest'
            response = requests.get(url, params={"amount": amount})
            data = response.json()
            asian_currencies_amt = {}
            available_rates = data["rates"].keys()
            for currency in currencies_in_asia:
                if currency in available_rates:
                    asian_currencies_amt[currency] = data["rates"][currency]
            
            return {
              "base": data["base"],
              "amounts": asian_currencies_amt
            }
        else:
            return {
              "message": "An error may have occured, did you access it via the frontend?"
            }
    except:
        return {"status": "error", "message": "An error occured."}
