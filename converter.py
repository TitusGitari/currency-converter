# converter.py
# A simple currency converter using ExchangeRate API

import requests  # to fetch exchange rate data

# Free API endpoint
API_URL = "https://api.exchangerate-api.com/v4/latest/"

# Ask user for base currency and target currency
base_currency = input("Enter base currency (e.g. USD): ").upper()
target_currency = input("Enter target currency (e.g. EUR): ").upper()
amount = float(input("Enter amount to convert: "))

# Fetch exchange rates for the base currency
response = requests.get(API_URL + base_currency)
data = response.json()

# Check if request worked
if "rates" in data:
    # Get the target currency rate
    if target_currency in data["rates"]:
        rate = data["rates"][target_currency]
        result = amount * rate
        print(f"\n{amount} {base_currency} = {result:.2f} {target_currency}")
    else:
        print("Target currency not found.")
else:
    print("Invalid base currency or API issue.")
