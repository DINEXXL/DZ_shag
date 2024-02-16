import requests

class CurrencyConverter:
    def __init__(self):
        self.rates = {}

    def get_rates(self):
        response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json") 
        data = response.json()
        for item in data:
            self.rates[item['cc']] = item['rate']

    def convert(self, amount):
        return round(amount / self.rates["USD"], 2)

converter = CurrencyConverter()
converter.get_rates()

while True:
    try:
        amount = float(input("Введіть суму: "))
        converted_amount = converter.convert(amount)
        print(f"{amount} дорівнює {converted_amount:.2f} USD")
        break
    
    except ValueError:
        print("Введено недійсну суму. Будь ласка, спробуйте ще раз.")